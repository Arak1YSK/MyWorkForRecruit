from django import forms
from django.contrib.auth.models import User
from .models import Account

# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        model = User
        fields = ('username','email','password',)
        labels = {'username':"ユーザーID",'email':"メール",}

class AddAccountForm(forms.ModelForm):
    class Meta():

        model = Account
        fields = ('last_name','first_name','status',)
        labels = {'last_name':"苗字",'first_name':"名前",'status':'状態',}

