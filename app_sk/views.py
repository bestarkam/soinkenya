from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context={
        'current_page' : 'index'
    }
    return render(request, 'app_sk/index.html', context)