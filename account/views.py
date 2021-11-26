from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from account.forms import LoginForm


def account_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)

                return redirect('main:index')

            form.add_error('password', "Login va/yoki parol noto'g'ri.")

    return render(request, 'account/login.html', {
        'form': form
    })


def account_logout(request):
    logout(request)

    return redirect('main:index')
