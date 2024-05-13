from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='news_picture/')
    description = models.TextField()
    timestamp = models.DateField(auto_now=True)
    
    @property
    def get_short_desc(self):
        return self.description[:130]
    def __str__(self):
        return self.title