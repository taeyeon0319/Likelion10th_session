from django.db import models
from django.contrib.auth.models import User
# receiver와 post_save import 하기

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # followings = 


# ↓ user생성 시 자동으로 profile이 생성되고 저장될 수 있도록 함 ↓
"""
@receiver(post_save, sender=User)
def create_user_profile():

@receiver(post_save, sender=User)
def save_user_profile():

"""