from django.shortcuts import render
from .models import UserModel
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages


def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        email = request.POST.get("email")

        if password == password1:
            user = User.objects.filter(username=username)
            if user.exists():
                messages.info(request, "Username already exists")
                return redirect("/register/")

            else:
                myuser = User.objects.create_user(
                    username,
                    email,
                    password,
                )
                myuser.save()
                messages.info(request, "Account created successfully")
                return redirect("/register/")
        else:
            messages.error(request, "Password and confirm password are mismatched")
    return render(request, "register.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("password")
        print(username, pass1)

        if not User.objects.filter(username=username).exists():
            messages.error(request, "invalid username")
            return redirect("/login/")

        user = authenticate(request, username=username, password=pass1)
        print(user)

        if user is None:
            messages.error(request, "invalid password")
            return redirect("/login/")

        else:
            login(request, user)
            return redirect("home")
    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect("/login/")


def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if User.objects.filter(email=email).exists():
            return redirect("/resetpass/")
        else:
            messages.error(request, "email id not found")
    return render(request, "forgotpass.html")


# def reset_passwords(request, User):
#     if request.method == "POST":
#         newpass = request.POST.get("newpass")
#         newpass1 = request.POST.get("newpass1")

#         if newpass1 == newpass:
#             if User:
#                 User.set_password(newpass)
#                 User.save()
#                 return redirect("/login/")
#     return render(request, "resetpass.html")


def reset_password(request):
    if request.method == "POST":
        newpass = request.POST.get("newpass")
        newpass1 = request.POST.get("newpass1")

        if newpass == newpass1:
            # Retrieve the user from the reset token (assuming you have implemented this).
            # If you haven't implemented token-based password reset, you should
            # prompt the user for their email again and retrieve the user based on that.

            # For this example, we'll assume you have a 'user' object.

            user = None  # Initialize the user variable
            if user:
                # Set the user's password using set_password method.
                user.set_password(newpass)
                user.save()
                # Log the user in automatically after resetting the password.
                user = authenticate(username=User.username, password=newpass)
                if user is not None:
                    login(request, user)
                return redirect("/login/")
            else:
                messages.error(request, "User not found")
        else:
            messages.error(request, "Passwords do not match")

    return render(request, "resetpass.html")
