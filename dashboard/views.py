from django.db.models import Sum
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from dashboard.models import Category

class HomePageView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = Category.objects.filter(author = self.request.user).prefetch_related(
            'payments').annotate(payments_sum = Sum('payments__summa'))
        return queryset

    