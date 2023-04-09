from django.urls import path
from .import views

urlpatterns = [
    path('', views.signup_view, name='signin'),
    path('login/', views.login_view, name='login'),
    path('about/', views.about_view, name='about'),
    path('seller/', views.seller_view, name='seller'),
    path('service/', views.service_view, name='service'),
    path('home/', views.home_view, name='home'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('contact', views.contact_view, name='contact'),
    path('logout', views.logout_view, name='logout'),
]
