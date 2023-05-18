from django.db import models
from django.contrib.auth.models import User

# ユーザーアカウントのモデルクラス
class Account(models.Model):
    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username