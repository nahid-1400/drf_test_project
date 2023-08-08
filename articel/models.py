from django.db import models
from django.contrib.auth.models import User


class CateGory(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    parent = models.ForeignKey('self', default=None, blank=True, null=True, on_delete=models.CASCADE, related_name='children', verbose_name='والد')


    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title

 


# Create your models here.
class Articel(models.Model):
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name='articles', verbose_name='نویسنده')
    STATUS_CHOICES = (
        ('d', ' پیش نویس'),
        ('p', 'منتشر شده'),
        ('i', 'در حال بررسی'),
        ('b', 'برگشت داده شده'),
    )
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='image_post', verbose_name='تصویر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')
    category = models.ManyToManyField(CateGory, verbose_name='دسته بندی', related_name='post_category')



    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات '


    def __str__(self):
        return self.title


