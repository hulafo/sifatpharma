from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pharma/home.html')
def about(request):
    return render(request, 'pharma/aboutus.html')
def contact(request):
    return render(request,'pharma/contact.html')