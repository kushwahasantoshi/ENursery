from django.urls import path
from . import views

urlpatterns = [
    path('', views.Welcome, name="home"),
    path('products/',views.products,name="products"),
    path('contact/',views.contact,name="contact"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('registration/',views.registration,name="registration"),
    path('login/',views.login_view,name="login"),
    path('user/',views.user,name="user"),
    path('logout/',views.logout_view,name="logout"),
]
