from django.shortcuts import render, redirect, reverse
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm


def index(request):
    """A view to display the index page"""
    return render(request,  'index.html')


@login_required
def logout(request):
    """A view to log the user out and redirect back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """A view to manage the login form"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            messages.success(request, "You have successfully logged in!")

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(
                    None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def register(request):
    """A view to manage the registration form"""
    registration_form = UserRegistrationForm()
    return render(request, 'register.html', {"registration_form": registration_form})
