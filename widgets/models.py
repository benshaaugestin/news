from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from news.models import News


class Subscribers(models.Model):
    email = models.EmailField(unique=True)
    token = models.CharField(max_length=36, null=True)
    active= models.BooleanField(default=False)

    def __str__(self):
        return self.email



@receiver(post_save, dispatch_uid="news_update", sender=News)
def my_handler(sender, instance,  **kwargs):
    template = loader.get_template('widgets/newsletter.html')
    context = { 'news': instance }
    message = template.render(context)
    send_mail(
        'The News Reporter! News Published ! %s'%instance.title,
        message,
        'newsletter@Thenewsreporter.in',
        list_of_subscribers(),
        fail_silently=False
        )
    return HttpResponse("Entered Signal")

post_save.connect(my_handler, sender=News)



def list_of_subscribers():
    ls = Subscribers.objects.all()
    return [n for n in ls]



class Contact(models.Model) :
    name=models.CharField(max_length=40)
    email=models.EmailField()
    message=models.CharField(max_length=300)

    def __str__(self):
        return self.name


