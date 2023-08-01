from django.shortcuts import render
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home/home.html", {})

# Create your views here.
