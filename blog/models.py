from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    focus = models.CharField(max_length=200)
    low_price = models.IntegerField()
    high_price = models.IntegerField()
    text = models.TextField()
    made_in = models.CharField(max_length=200)
    based_in = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
#    image1_url = models.CharField(max_length=200, default='default_1.jpg')
#    image2_url = models.CharField(max_length=200, default="default_1.jpg")
    image = models.FileField(blank=True)

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.company_name
