from django.conf.urls import url,include
from django.views.generic import ListView,DetailView
from pharma.models import Post
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
   
    url(r'^$',views.index,name='index'),
   url(r'^about/',views.about,name='about'),
   
    url(r'^blog/', ListView.as_view(model=Post,queryset=Post.objects.all().order_by("-date")[:25],
                               template_name="pharma/blog/blog.html")),
    url(r'^post/(?P<pk>\d+)$', DetailView.as_view(model=Post,template_name='pharma/blog/post.html')),
    url(r'^post/',views.post,name='post'),
   
    #url(r'^blog/',views.blog,name='blog'),
    url(r'^contact/',views.contact,name='contact'),
   #url(r'^pharma_en/',include('pharma_en.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
