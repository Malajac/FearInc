from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='News title')
    content = models.TextField(blank=True, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Published on')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated on')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Published?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News item'
        verbose_name_plural = 'News list'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Category title")

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category list'
        ordering = ['title']
