from django.shortcuts import render # type: ignore
from .models import Store

# Create your views here.
def all_stores(request):
    return render(request, 'store_list.html', {'stores': Store.objects.all()})