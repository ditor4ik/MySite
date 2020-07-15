from django.db.models import F
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import PersonCreateView, SignInView
from .models import User


def CheckInForm(request):
    if request.method == 'POST':
        user_form = request.POST
        EMAIL = user_form.getlist('email')[0]
        NN = user_form.getlist('NickName')[0]
        password = user_form.getlist('Password')[0]
        NEWUSER = User(email=EMAIL, NickName=NN, Password=password)
        FindObject = User.objects.filter(email=EMAIL)
        ErrNN = False
        ErrE = False
        if (FindObject.count() > 0): ErrE = True

        FindObject = User.objects.filter(NickName=NN)

        if (FindObject.count() > 0): ErrNN = True

        if ( ErrNN or ErrE):
            user_form = PersonCreateView()
            return render(request, 'CheckIn/base.html', {'form': user_form, 'NickNameError': ErrNN, 'emailError': ErrE})

        else:
            NEWUSER.save()
            return render(request, 'CheckIn/success.html', {'new_user': user_form})

    else:
        user_form = PersonCreateView()
        return render(request, 'CheckIn/base.html', {'form': user_form, 'NickNameError': False, 'emailError': False})


def SignInForm(request):
    if request.method == 'POST':
        user_form = request.POST
        Nick = user_form.getlist('NickName')[0]
        Pass = user_form.getlist('Password')[0]
        FindObject = User.objects.filter(NickName=Nick)
        if(FindObject.count() > 0):
            FindObject = User.objects.get(NickName=Nick)
            if (FindObject.Password == Pass):
                request.session['NickName'] = Nick
                return redirect(reverse('HomePage:index'))
        user_form = SignInView()
        return render(request, 'SignIn/base.html', {'form': user_form, 'SignInError': True})
    else:
        user_form = SignInView()
        return render(request, 'SignIn/base.html', {'form': user_form, 'SignInError': False})

def Logout(request):
    del request.session['NickName']
    return redirect(reverse('HomePage:index'))

# Create your views here.
