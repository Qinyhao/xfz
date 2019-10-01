
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from shortuuidfield import ShortUUIDField
from django.db import models

#自定义用户管理类
class UserManager(BaseUserManager):

    def _create_user(self,telephone,username,password,**kwargs):
        if not telephone:
            raise ValueError('请传入手机号码')
        if not password:
            raise ValueError('请传入密码')
        if not username:
            raise ValueError('请传入用户名')
        #创建用户并保存
        user = self.model(telephone=telephone,username=username,**kwargs)
        user.set_password(password)
        user.save()
        return user
    #创建普通用户，is_superuser为False
    def create_user(self,telephone,username,password,**kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone,username,password,**kwargs)
    #创建超级用户
    def create_superuser(self,telephone,username,password,**kwargs):
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(telephone,username,password,**kwargs)

#定义用户模型
class User(AbstractBaseUser,PermissionsMixin):
    # 使用shortuuid
    uid = ShortUUIDField(primary_key=True)#shotuuid，主键
    telephone = models.CharField(max_length=11,unique=True)#手机号
    password = models.CharField(max_length=200)#密码
    email = models.EmailField(unique=True,null=True)#电子邮箱
    username = models.CharField(max_length=100)#用户名
    is_active = models.BooleanField(default=True)#账户是否有效
    is_staff = models.BooleanField(default=False)#是否为员工，是员工可登陆后台
    data_joined = models.DateTimeField(auto_now_add=True)#注册时间

    USERNAME_FIELD = 'telephone'
    # telephone，username，password
    REQUIRED_FIELDS = ['username']
    EMAIL_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
