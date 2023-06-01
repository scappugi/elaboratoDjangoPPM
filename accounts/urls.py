from django.urls import path

from accounts.views import ProfileView
from . import views

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path('register/', views.register_user, name="register")
]
