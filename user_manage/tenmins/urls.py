"""tenmins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from website.api import *
from website.mobile_views import *
from django.conf import settings #DEBUG环境需要加
from django.conf.urls.static import static #DEBUG环境需要加

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^m/userdetail/',userdetail,name='userdetail'),
    url(r'^m/userlistpanel/login',userListLogin,name='userListLogin'),
    url(r'^m/userlistpanel/$',userListPanel,name='userListPanel'),



    # api部分
    url(r'^api/login/',login),# 登录
    url(r'^api/user/',user),# 获取用户列表
    url(r'^api/adduser/',adduser),# 添加用户
    url(r'^api/deleteuser/(?P<id>\d+)',deleteuser),# 删除用户
    url(r'^api/inviteduser/(?P<id>\d+)',invited),# invited user
    url(r'^api/banuser/(?P<id>\d+)',ban_user), # 禁止用户登录
    url(r'^api/detail/(?P<id>\d+)',user_detail),# 获取用户详情
    url(r'^api/changeuserinfo/(?P<id>\d+)',change_user_info), # 修改用户名及密码
    url(r'^api/logout/',logout),# 退出登录
]

#DEBUG环境需要加
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

