from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pharma_en/home.html')
def about(request):
    return render(request, 'pharma_en/aboutus.html')
def contact(request):
    return render(request,'pharma_en/contact.html')
