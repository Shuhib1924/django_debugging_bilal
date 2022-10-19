from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image", default='default.jpg')
    changeName = models.CharField(max_length=100, default='lost Name')

    def __str__(self):
        return self.changeName

    def save(self, *args, **kwargs):
        super().save(*args, *kwargs)

        img = Image.open(self.image.path)
        if img.height > 200 or img.width > 200:
            img.thumbnail((200, 200))
            img.save(self.image.path)
