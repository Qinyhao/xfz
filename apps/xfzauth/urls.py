from django.urls import path
from . import views

app_name='xfzauth'

urlpatterns = [
    path('login/',views.login_view,name = 'login'),
    path('create/',views.createuser,name = 'create'),
    path('logout/',views.logout_view,name = 'logout'),
    path('img_captcha/',views.img_captcha,name = 'img_captcha'),
    path('sms_captcha/',views.sms_captcha,name = 'sms_captcha'),
    path('register/',views.register,name = 'register'),
    path('cache/',views.cache_text,name = 'cache'),
]