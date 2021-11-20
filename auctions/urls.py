from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("makeBid/<int:item_id>", views.makeBid, name="makeBid"),
    path("newComment/<int:item_id>", views.newComment, name="newComment"),
    path("closeListing/<int:item_id>", views.closeListing, name="closeListing"),
    path("changeWatchList/<int:item_id>",
         views.changeWatchList, name="changeWatchList"),
    path("create", views.create, name="create"),
    path("listing/<int:item_id>", views.listing, name="listing"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
