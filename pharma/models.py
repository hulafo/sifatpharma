from django.db import models
#from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=140)
    shortbd=models.TextField()
    body=models.TextField()
    image=models.ImageField(upload_to='blog/%Y/%m/%d/',blank=True)
    date=models.DateTimeField()
    
    
    def __str__(self):
        return self.title
   