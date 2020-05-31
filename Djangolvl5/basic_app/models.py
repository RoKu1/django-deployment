from django.db import models
from  django.contrib.auth.admin import User

# Create your models here.
class  userprofileinfo(models.Model):
    user =  models.OneToOneField(User,on_delete=models.NullBooleanField)


    profile_link = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profiles',blank=True)

    def __str__(self):
        return self.user.username