from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.


def UserRegister(request):

    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            subject = "Başarılı Kayıt"
            message = f"Kullanıcı kaydı başarıyla oluşturuldu"

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [form.email]
            )



            form.save()
            messages.success(request, "Kayıt Başarılı")
            return redirect('login')

    context = {
        'form':form
    }


    return render(request, "register.html", context)


def userLogin(request):

    if request.method == "POST":
        username = request.POST['kullanici']
        password = request.POST['sifre']

        user = authenticate(request,username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "Giriş yapıldı.")
            return redirect("index")
        else:
            return redirect('login')
            

    return render(request, "login.html")



def userLogout(request):
    logout(request)
    messages.success(request, "Çıkış yapıldı")
    return redirect('login')


def passwordChange(request):
        
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            logout(request)
            messages.success(request, "Şifre değiştirme işlemi paşarılı")
            return redirect('login')
        else:
            messages.error(request, "Girdiğiniz bilgiler hatalı")
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form':form
    }

    return render(request, "password_change.html",context)


def account_delete(request):
    user = request.user

    if request.method == "POST":
        if user.is_authenticated:
            user = request.user
            user.delete()
            logout(request)
            messages.success(request, "Hesabınız Silindi")
            return redirect('index')
        else:
            messages.error(request, "Hesabı silmek için giriş yapmalısınız!")
            return redirect('login')
        
    return render(request, 'account_delete.html')