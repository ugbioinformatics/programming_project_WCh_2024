from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Post
import shutil
import os


@receiver(post_delete, sender=Post)
def delete_on_post_del(sender, instance, **kwargs):
    try:
        if os.path.isdir('media/'+instance.plik_hash):
            shutil.rmtree('media/'+instance.plik_hash)
    except:
        print('error deleting file')
        print(instance.plik_hash)
