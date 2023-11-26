from django.shortcuts import render, redirect
from .forms import UserForm, PageForm, SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as dj_login, authenticate
# Create your views here.


def index(request):
    content = {
        "title": "Paracelsus",
    }
    return render(request, "main/index.html", content)


def registration(request):
    content = {
        "title": "Регистрация",
    }
    return render(request, "main/registration.html", content)


def login(request):
    content = {
        "title": "Вход",
    }
    return render(request, "main/login.html", content)


def user_calendar(request):
    content = {
        "title": "Календарь",
    }
    return render(request, "main/user-calendar.html", content)


# Пока не разобрались с ошибкой (если я не написала про неё, сигналь), сделала свои вьюшки, а там их отредачим

def register_user(request):

    msg = None

    if request.method == "POST":

        form = SignUpForm(request.POST)

        if form.is_valid():

            # Create the user
            form.save()

            msg = 'User created successfully.'

        else:
            msg = 'Form is not valid'

    else:
        form = SignUpForm()

    return render(request, "main/register.html", {"form": form, "msg" : msg })


def betalogin(request):

    if request.method == "GET":
        form = LoginForm()
        return render(request, "main/betalogin.html", {"form": form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                dj_login(request, user)
                messages.success(request, f"Hi {username.title()}, welcome back!")
                return redirect("main/testlogin")

        messages.error(request, f"Invalid username or password")
        return render(request, "main/betalogin.html", {"form": form})


@login_required
# @transaction.atomic
def testlogin(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        page_form = PageForm(request.POST, instance=request.user.page)
        if user_form.is_valid() and page_form.is_valid():
            user_form.save()
            page_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('main/success.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        page_form = PageForm(instance=request.user.page)

    return render(request, 'main/test_login.html', {
            'user_form': user_form,
            'page_form': page_form
        })
