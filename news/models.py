from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='News title')
    content = models.TextField(blank=True, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Published on')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated on')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo')
    is_published = models.BooleanField(default=True, verbose_name='Published?')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News item'
        verbose_name_plural = 'News list'
        ordering = ['-created_at']
