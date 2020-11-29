from django.urls import include ,path
from . import views, forms_ls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),

    path("discover/", views.discover, name="discover"),
    path("about_us/", views.about_us, name="about_us"),
    path("requestDrive/", views.request_drive, name="request_drive"),

    path("donate/", forms_ls.donate_form, name="donateNow"),

    path("thank_you_user/", forms_ls.donate_form, name="Thankyou"),
    path("login/", forms_ls.login_per, name="login"),
    
]