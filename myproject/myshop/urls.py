from django.urls import path
from . import views

urlpatterns = [
    path('', views.allproducts, name='allproducts'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('contact/', views.contact_details, name='contact'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('product/<slug:slug_cat>/', views.allproducts, name='product_by_category'),
    path('product/<slug:slug_cat>/<slug_prod>/', views.cat_prod, name='product_details'),

]
