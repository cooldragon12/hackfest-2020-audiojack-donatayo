from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "BeniFaction/index.html", {
    })

def discover(request):
    return render(request, "BeniFaction/discover.html",{
    })

def about_us(request):
    return render(request, "BeniFaction/about_us.html",{})

def request_drive(request):
    return render(request, "Benifaction/requst_backup.html",{})
