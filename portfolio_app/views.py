from django.shortcuts import render
from django.http import HttpResponse
def portfolio(request):
    return render(request, 'portfolio_app/index.html')

def index(request):
    return HttpResponse('home page')
# Create your views here.
