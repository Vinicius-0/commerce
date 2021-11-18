from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Listing, User


def index(request):
    items = Listing.objects.all()
    return render(request, "auctions/index.html", {
        'items': items
    })


def create(request):
    if request.method == 'POST':
        item = Listing()
        item.creator = request.user.username
        item.title = request.POST.get('title')
        item.category = request.POST.get('category')
        item.description = request.POST.get('description')
        item.initialBid = request.POST.get('initialBid')
        item.image = request.POST.get('image') if request.POST.get(
            'image') else 'https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg'
        item.save()
        return HttpResponseRedirect(reverse("index"))

    return render(request, "auctions/create.html")


def handle_uploaded_file(f):
    destination = open('static/images/images/', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
