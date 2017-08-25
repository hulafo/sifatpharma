from django.shortcuts import render, get_object_or_404,render_to_response
from .models import Post
# Create your views here.
def index(request):
    post=  Post.objects.all()
    return render(request,'pharma/home.html',{
        'post':post})
def about(request):
    return render(request, 'pharma/aboutus.html')
def contact(request):
    return render(request,'pharma/contact.html')
def blog(request):
    return render(request,'pharma/blog/blog.html')
def post(request):
   
    return render(request,'pharma/blog/post.html')
    
    
    
    
    