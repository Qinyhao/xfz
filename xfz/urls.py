"""xfz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from apps.news import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index,name='index'),#主页
    path('search/',views.search,name = 'search'),#搜索页
    path('news/', include("apps.news.urls")),#语新闻相关url
    path('cms/', include("apps.cms.urls")),#内容管理相关url
    path('account/', include("apps.xfzauth.urls")),#账户相关
path('course/', include("apps.course.urls")),#课程相关
path('payinfo/',include("apps.payinfo.urls")),#付费相关
path('ueditor/',include("apps.ueditor.urls")),#发布新闻页编辑器
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path("__debug__/",include(debug_toolbar.urls)))

