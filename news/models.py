from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.shortcuts import reverse
from django.core.files.storage import FileSystemStorage




class Category(models.Model):
    category_name=models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('news:category',kwargs={'pk':self.pk})

class News(models.Model):
    title= models.CharField(max_length=200)
    content=models.CharField(max_length=750)
    author=models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE ,blank=True, null=True)
    pub_date = models.DateTimeField()
    photo = models.ImageField(upload_to='src/' ,blank=True, null=True)

    class Meta:
        ordering = ["-pub_date"]
        verbose_name_plural ="News"

    def get_absolute_url(self):
        return reverse('news:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()




