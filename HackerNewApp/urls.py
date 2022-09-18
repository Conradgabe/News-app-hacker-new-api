from django.urls import path
from . import views

urlpatterns = [
    path('', views.make_request, name='make_request'),
    path('list', views.ItemList.as_view(), name='item-list'),
    path('filter', views.ItemFilter.as_view(), name='item-filter'),
    path('search', views.ItemSearch.as_view(), name='item-search'),
]