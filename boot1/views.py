from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def product(request):
    return render(request, 'product.html')

def video(request):
    return render(request, 'video.html')

def remot(request):
    return render(request, 'remot.html')

# Create your views here.
