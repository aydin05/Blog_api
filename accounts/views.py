from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import auth
from django.shortcuts import render, redirect
from django.views.generic import FormView

from myapp.forms import RegisterForm


def login(request):
    if request.method == 'POST':
        print(request.POST)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
"""


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


"""
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                print('user created')
                send_mail(
                    'Send mail',
                    'Welcome my  Blog',
                    'aydin.aliyev058@gmail.com',
                    [email]
                )
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')

"""


def logout(request):
    auth.logout(request)
    return redirect('/')
