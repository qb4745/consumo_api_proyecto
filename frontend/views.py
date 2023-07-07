from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView
import requests

class HomeListView(ListView):
    paginate_by = 50
    template_name = "frontend/home.html"
    context_object_name = "data"

    def get_queryset(self):
        response = requests.get(f'http://127.0.0.1:8000/api/onepiececapitulomanga/')
        if response.status_code == 200:
            data = response.json()
            return data['results']
        return []

