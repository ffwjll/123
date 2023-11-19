from django.db import models
from django.urls import reverse


class Post(models.Model):
    name = models.CharField(max_length=30)
    likes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images/')
    content = models.TextField()

    def __str__(self):
        return f'{self.id} | {self.name}'
    #
    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})


