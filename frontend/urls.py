from django.urls import path
from .views import HomeListView

app_name = 'frontend'

urlpatterns = [
    path('', HomeListView.as_view(), name='frontend-home'),
    ]