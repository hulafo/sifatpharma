from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pharma_tj/home.html')
def about(request):
    return render(request, 'pharma_tj/aboutus.html')
def contact(request):
    return render(request,'pharma_tj/contact.html')
