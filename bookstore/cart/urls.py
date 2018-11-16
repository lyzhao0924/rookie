from django.conf.urls import url 
from cart import views

urlpatterns=[
    url(r'^add/$',views.cart_add,name='add'),#t添加购物车数据
    url(r'^count/$',views.cart_count,name='count'),#huo获取购物车商品数量
    url(r'^del/$',views.cart_del,name='delete'),#删除购物车商品记录
    url(r'update/$',views.cart_update,name='update'),#更新购物车商品数目
    url(r'^&',views.cart_show,name='show'),#显示用户购物车页面

]




