from django.urls import path

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('accounts/signup', HomePageView.as_view(), name='signup'),
    path('accounts/login', HomePageView.as_view(), name='login'),
]