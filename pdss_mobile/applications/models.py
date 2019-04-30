from django.db import models


def upload_to(instance, filename):
    extension = filename.split('.')[-1]
    # 因为根目录为 MEDIA_URL = '/uploads/'；
    # MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")；
    # 所以返回根目录路径/uploads/name/version.extension
    return "{0}/{1}.{2}".format(instance.name, instance.version, extension)


# Create your models here.
class App(models.Model):
    name = models.CharField(max_length=200)
    version = models.CharField(max_length=10)
    released_at = models.DateField()
    file = models.FileField(upload_to=upload_to)
