from django.urls import path

from dashboard.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home')
]