from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from Store.models import Products

urlpatterns = [
    url(r'^$', ListView.as_view(queryset = Products.objects.all().order_by('title'),template_name = 'page/page.html'))
]