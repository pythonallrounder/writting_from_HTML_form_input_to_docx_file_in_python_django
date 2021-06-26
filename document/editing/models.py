from django.db import models

# Create your models here.

class Document(models.Model):
    
    com_name = models.CharField(max_length=50) 
    srt_name = models.CharField(max_length=50)  
    scope = models.CharField(max_length=150)
    date = models.DateField()
    img = models.ImageField(upload_to='pics')
    
class FilesAdmin(models.Model):
    adminupload = models.FileField(upload_to='media')
    title = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.title
    
    
