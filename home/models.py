from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from user_module.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    name = models.CharField(max_length=100, verbose_name='مهارت')
    score = models.IntegerField(verbose_name='میزان مهارت', validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'مهارت'
        verbose_name_plural = 'مهارتها'


class Tools(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    name = models.CharField(max_length=100, verbose_name='ابزار')
    score = models.IntegerField(verbose_name='میزان مهارت', validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ابزار'
        verbose_name_plural = 'ابزارها'


class Projects(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام پروژه')
    description = models.TextField(verbose_name='توضیحات')
    skill = models.ManyToManyField(Skill, verbose_name='ابزار استفاده شده')
    url = models.URLField(max_length=300, verbose_name='لینک پروژه')
    github_url = models.URLField(max_length=300, verbose_name='کد منبع در گیت هاب')
    img = models.ImageField(verbose_name='تصویر', upload_to='images/projects')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'نمونه کار'
        verbose_name_plural = 'نمونه کارها'


class TimeLineRoad(models.Model):
    skill = models.OneToOneField(Skill, on_delete=models.CASCADE, verbose_name='مهارت', null=True, blank=True)
    project = models.OneToOneField(Projects, on_delete=models.CASCADE, verbose_name='پروژه', null=True, blank=True, editable=True)
    start_date = models.DateField(verbose_name='تاریخ شروع یادگیری')
    short_description = models.CharField(max_length=300, verbose_name='توضیح کوتاه')
    descriptions = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return f'{self.short_description}'

    class Meta:
        verbose_name = 'مسیر یادگیری'
        verbose_name_plural = 'مسیرهای یادگیری'


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url', unique=True, allow_unicode=True, editable=False)
    short_descriptions = models.CharField(max_length=300, verbose_name='توضیحات کوتاه')
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر')
    category = models.ForeignKey(Skill, verbose_name='دسته بندی', on_delete=models.PROTECT, null=True, blank=True)
    content = CKEditor5Field(verbose_name='متن', config_name='extends', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


class ContactUsModel(models.Model):
    STATUS_CHOICES = [
        ('new', 'جدید'),
        ('read', 'خوانده شده'),
        ('answer', 'پاسخ داده شده'),
        ('closed', 'بسته شده'),
    ]

    name = models.CharField(max_length=100, verbose_name='نام')
    email = models.EmailField(max_length=200, verbose_name='ایمیل')
    message = models.TextField(verbose_name='پیام کاربر')
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='new', verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد پیام')

    admin_reply = models.TextField(verbose_name='پاسخ ادمین', null=True, blank=True)
    replied_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='cmessage_replied_by_admin')
    replied_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}: {self.message}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'پیام ارتباط با ما'
        verbose_name_plural = 'پیام های ارتباط با ما'


class SocialLinks(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    link = models.URLField(max_length=300, verbose_name='لینک')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'راه ارتباطی'
        verbose_name_plural = 'راه های ارتباطی'