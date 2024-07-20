from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'static_assets/home.html')

def index(request):
    return render(request, 'static_assets/index.html')

