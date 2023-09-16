from django.urls import path
from . import views

# Wire up apiour API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.CurrencyListView.as_view(), name='current_list'),
    path('form/', views.currency_volume, name='currency_volume')
]
