from django.urls import path

from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("home", views.home, name="home"),
    path("viewTransactions", views.viewTransactions, name="viewTransactions"),
    path("addTransaction", views.addTransaction, name="addTransaction"),
    path("logout", views.logout, name="logout"),
]