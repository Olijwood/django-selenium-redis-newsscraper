from django.db import models

# Create your models here.
class NewsItem(models.Model):
    source = models.CharField(max_length=100)
    link = models.TextField()
    title = models.CharField(max_length=400)
    publish_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link[0:50]
    
class ScrapeRecord(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.timestamp}'