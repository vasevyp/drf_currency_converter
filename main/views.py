from django.shortcuts import render
from django.views.generic import ListView
import requests

from .models import CurrencyRate
from .forms import VolumeForm


class CurrencyListView(ListView):
    model = CurrencyRate
    template_name = 'index.html'
    context_object_name = 'currency_list'

    def get_context_data(self, **kwargs):
        my_currency = 'RUB'
        context = super().get_context_data(**kwargs)
        context['date_rate'] = requests.get(
            f"https://open.er-api.com/v6/latest/{my_currency}").json()['time_last_update_utc']
        return context


def currency_volume(request):
    # currency_volume = CurrencyRate.objects.all()
    currency_volume = requests.get(
        'http://localhost:8000/api/currency-rate/').json()
    input_data = request.GET['fulltextarea']
    if input_data:
        data = input_data
    else:
        data = 1
    print(data)

    return render(request, 'index.html', {'data': data, 'currency_volume': currency_volume})
