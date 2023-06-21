from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Image(models.Model):
    '''
    Модель Image
    '''

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='images_created')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            blank=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created'])
            ]
        ordering = ['-created']

    def __str__(self):
        return self.title
