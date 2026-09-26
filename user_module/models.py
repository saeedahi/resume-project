from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True, verbose_name='شماره همراه')
    about_user = models.TextField(verbose_name='درباره کاربر')
    more_about_me = models.TextField(verbose_name='بیشتر درباره کاربر', null=True, blank=True)

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
