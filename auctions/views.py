from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Comment, Listing, User, Bid


def index(request):
    category = request.GET.get('category', '')
    if category:
        items = Listing.objects.filter(
            isActive=True, category=category)
        return render(request, "auctions/index.html", {
            'items': items,
            'category': category
        })
    else:
        items = Listing.objects.filter(isActive=True)
        return render(request, "auctions/index.html", {
            'items': items,
        })


@login_required(login_url='/login')
def watchlist(request):
    category = request.GET.get('category', '')
    if category:
        itemsCategory = Listing.objects.filter(category=category)
    else:
        itemsCategory = Listing.objects.filter()
    itemsWatched = request.user.watchedListings.all()
    items = set(itemsCategory) & set(itemsWatched)
    return render(request, "auctions/index.html", {
        'watchlist': True,
        'items': items,
        'category': category
    })


@login_required(login_url='/login')
def changeWatchList(request, item_id):
    item = Listing.objects.get(id=item_id)
    if request.user in item.watchers.all():
        item.watchers.remove(request.user)
    else:
        item.watchers.add(request.user)
    return redirect('listing', item_id)


@login_required(login_url='/login')
def closeListing(request, item_id):
    item = Listing.objects.get(id=item_id)
    if request.user.username == item.creator:
        item.isActive = False
        item.winner = Bid.objects.filter(
            listingID=item_id).last().user
        item.save()
    return redirect('listing', item_id)


@login_required(login_url='/login')
def makeBid(request, item_id):
    item = Listing.objects.get(id=item_id)
    bid = float(request.GET.get('bid'))
    if bid >= item.initialBid and (item.actualBid == 0 or bid > item.actualBid):
        item.actualBid = bid
        item.save()
        bidItem = Bid()
        bidItem.user = request.user
        bidItem.offer = bid
        bidItem.listingID = item
        bidItem.save()
        if request.user not in item.watchers.all():
            item.watchers.add(request.user)
        return HttpResponseRedirect(reverse('listing', args=[item_id]))
    else:
        actual = item.actualBid if item.actualBid > 0 else item.initialBid
        return render(request, "auctions/listing.html", {
            'item': item,
            'watched': request.user in item.watchers.all(),
            'error': f'Your bid must be bigger than {actual}'
        })


@login_required(login_url='/login')
def newComment(request, item_id):
    item = Listing.objects.get(id=item_id)
    newComment = Comment()
    newComment.user = request.user
    newComment.comment = request.GET.get('comment')
    newComment.listingID = item
    newComment.save()
    return redirect('listing', item_id)


def listing(request, item_id):
    item = Listing.objects.get(id=item_id)
    comments = Comment.objects.filter(listingID=item_id).order_by('-dateTime')
    return render(request, "auctions/listing.html", {
        'item': item,
        'watched': request.user in item.watchers.all(),
        'comments': comments
    })


@login_required(login_url='/login')
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
