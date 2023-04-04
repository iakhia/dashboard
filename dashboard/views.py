from django.db.models import Sum
from django.views.generic import ListView, View, DetailView
from rest_framework.generics import ListAPIView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from dashboard.models import Category, Payment
from dashboard.serializers import CategorySerializer

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
  

class HomePageView(ListView):
    template_name = 'index.html'
    context_object_name = 'categories'

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return
        queryset = Category.objects.filter(author = self.request.user).prefetch_related(
            'payments').annotate(payments_sum = Sum('payments__summa'))
        return queryset

class CategoryAddView(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'category_add.html')
    
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('category')
        category = Category(name=name, author = request.user)
        category.save()
        return redirect('home')  
    
class PaymentAddView(DetailView):
    model = Category
    template_name = 'payment_add.html'
    
    
    
    def post(self, request, *args, **kwargs):
        summa = request.POST.get('summa')
        payment = Payment(summa=summa, category_id = kwargs.get('pk'))
        payment.save()
        return redirect('home')  
    