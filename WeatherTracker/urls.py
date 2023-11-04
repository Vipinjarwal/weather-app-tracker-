from django.contrib import admin
from django.urls import path
from weatherinfo import views
from user import views as userview


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("historical/", views.historical, name="historical"),
    path("service/", views.service, name="service"),
    path("question/", views.question, name="question"),
    path("contact/", views.contact, name="contact"),
    path("contactform/", views.contactform, name="contactform"),
    path("register/", userview.register_page, name="register"),
    path("login/", userview.login_page, name="login"),
    path("logout/", userview.logout_page, name="logout"),
    path("forgotpass/", userview.forgot_password, name="forgotpass"),
    path("resetpass/", userview.reset_password, name="resetpass"),
    # path("historicaldata/", views.historical_data, name="historical_data"),
]
