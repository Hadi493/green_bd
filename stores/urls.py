from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.all_stores, name='all_stores'),
]
