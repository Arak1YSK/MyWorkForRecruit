from django.shortcuts import render
from django.views.generic import TemplateView 
from .forms import AccountForm, AddAccountForm 
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Account

#ログイン
def Login(request):
    if request.method == 'POST':
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')
        user = authenticate(username=ID, password=Pass)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("アカウントが有効ではありません")
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    else:
        return render(request, 'App_Folder_HTML/login.html')


#ログアウト
@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login'))


#ホーム
@login_required
def home(request):
    account = request.user.account
    status = account.status
    if request.method == 'POST':
        if "enter" in request.POST:
            if status == True:
                msg = 'すでに入室しています'
            else:
                msg = '入室しました!!'
                account.status = True
                account.save()
        elif "exit" in request.POST:
            if status == False:
                msg = '入室していません'
            else:
                msg = '退出しました!お疲れさまです！'
                account.status = False
                account.save()
        else: 
            msg = "bug"
    else:
        msg = 'こんにちは'
    data = Account.objects.filter(status=True)
    params = {
        "UserID": request.user,
        "message": msg,
        "data": data,
    }
    return render(request, "App_Folder_HTML/home.html", context=params)



#新規登録
class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"App_Folder_HTML/register.html",context=self.params)

    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        #有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            account = self.params["account_form"].save()
            account.set_password(account.password)
            account.save()
 
            add_account = self.params["add_account_form"].save(commit=False)
            add_account.user = account
            add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            print(self.params["account_form"].errors)

        return render(request,"App_Folder_HTML/register.html",context=self.params)