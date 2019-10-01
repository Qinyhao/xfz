from django.contrib.auth import login,logout,authenticate
from django.views.decorators.http import require_POST
from .forms import LoginForm,RegisterForm
from django.http import JsonResponse
from .models import User
from utils import restful
from django.shortcuts import redirect,reverse,HttpResponse
from utils.captcha.xfzcaptcha import Captcha
from io import BytesIO
from utils.Tencentsdk import Tecent_sms_send
from utils import restful
from django.core.cache import cache
from django.contrib.auth import get_user_model

@require_POST
def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        password = form.cleaned_data.get('password')
        remember = form.cleaned_data.get('remember')
        user = authenticate(request,username=telephone,password=password)
        if user:
            if user.is_active:
                login(request,user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                return restful.ok()
            else:
                return restful.unauth(message="您的帐号已被冻结")
        else:
            return restful.params_error(message="手机号或密码错误")
    else:
        errors = form.get_errors()
        return restful.params_error(message=errors)

def createuser(request):
    try:
        user = User.objects.create_superuser(18888888881,'xpp','520xpp')
    except Exception:
        pass
    return JsonResponse({'message':'ss'})

def logout_view(request):
    logout(request)
    return redirect(reverse('index'))

#获取图片验证码
def img_captcha(request):
    text,image = Captcha.gene_code()
    #将图片存入字节流
    out = BytesIO()
    image.save(out,'png')
    #将Bytes文件指针移动到开始
    out.seek(0)
    response = HttpResponse(content_type='image/png')
    #从BytesIo中读取图片数据1，存到response上
    response.write(out.read())
    response['Content-length'] = out.tell()
    #将图形验证码存入memcached
    cache.set(text.lower(),text.lower(),5*60)

    return response
#发送短信验证码
def sms_captcha(request):
    telephone = request.GET.get('telephone')
    code = Captcha.gene_text()
    cache.set(telephone,code,5*60)
    # result = Tecent_sms_send.send_sms(telephone,code)
    print('短信验证码：',code)
    return restful.ok()

@require_POST
def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        try:
           user =User.objects.create_user(telephone=telephone,username=username,password=password)
        except Exception :
            pass
        login(request,user)
        return restful.ok()
    else:
        return restful.params_error(message=form.get_errors())



def cache_text(request):
    cache.set('username','xpp',60)
    result = cache.get('username')
    print(result)
    return HttpResponse('ss')


