from django.urls import path
from rest_framework.routers import DefaultRouter
from dashboard.views import HomePageView, CategoryAddView, PaymentAddView, CategoryViewSet



urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('category_add/', CategoryAddView.as_view(), name = 'category_add'),
    path('payment_add/<int:pk>/', PaymentAddView.as_view(), name = 'payment_add'),
]
router = DefaultRouter()
router.register('api/v1/categories', CategoryViewSet, basename= 'categories')
urlpatterns += router.urls



