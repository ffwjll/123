from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=30)
    embed_code = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} | {self.name}'
