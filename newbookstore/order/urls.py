"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from order import views

urlpatterns = [
    url(r'^place/$', views.order_place, name='place'), # 订单提交页面
    url(r'^commit/$', views.order_commit, name='commit'), # 生成订单
    url(r'^pay/$', views.order_pay, name='pay'), # 订单支付
    url(r'^check_pay/$', views.check_pay, name='check_pay'), # 查询支付结果
]
