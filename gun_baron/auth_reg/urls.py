from django.urls import path
from . import views

urlpatterns = [
	path('reg/', views.reg, name='reg'),
	path('', views.main, name='main'),
	path('auth/', views.auth, name='auth'),
	path('logout/', views.logout, name='logout'),
	path('products/<id>', views.products, name='products'),
	path('basket/', views.basket, name='basket'),
	path('purchase/', views.purchase, name='purchase'),
	path('buy/', views.buy, name='buy'),
	path('product/<slug:slug>', views.product, name='product'),
	path('profile/', views.profile, name='profile'),
	path('change_basket/', views.on_change_basket, name='change_basket'),
	path('finish/', views.finish, name='finish'),
	path('qr/', views.qr, name='qr'),
	path('delete_pr_basket', views.delete_from_basket, name='delete_pr_basket'),
	path('user-list/', views.UserViewSet.as_view(), name='user_view'),
	path('user-view/<pk>', views.UserView.as_view(), name='user'),
]
