"""
URL configuration for registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from soulsbornestore import views 
urlpatterns = [
    path('',views.home,name="home"),
    path('Login',views.Login,name="Login"),
    path('Adminuser',views.Adminuser,name="Adminuser"),
    path('Adminendpoint',views.Adminendpoint,name="Adminendpoint"),
    path('search',views.search,name="search"),
    path('adddata',views.adddata,name="adddata"),
    path('deldata',views.deldata,name="deldata"),
    path('modify',views.modifydata,name="modify"),
    path('userendpoint',views.userendpoint,name="userendpoint"),
    path('checkout',views.checkout,name="checkout"),
    path('cart',views.cart,name="checkout"),
    path('updateCart',views.updateCart,name="updateCart"),
    path('DeleteCart',views.DeleteCart,name="DeleteCart"),
    path("Create",views.Create,name="Create"),
    path("UserBack",views.UserBack,name="UserBack"),
    path("AuthorSearch",views.AuthorSearch,name="AuthorSearch"),
    path("PriceSearch",views.PriceSearch,name="PriceSearch"),
    path("UserHome",views.UserHome,name="UserHome"),
    path("NameSearch",views.NameSearch,name="NameSearch"),
    path("MoreInfo",views.MoreInfo,name="MoreInfo"),
    path("View",views.View,name="View"),
    path("GenreFilter",views.GenreFilter,name="GenreFilter"),
    path("Filterview",views.GenreView,name="Filterview") , 
    path("Sales",views.sales,name="Sales"),
    path("Review",views.reviews,name="Review"),
    path("ReviewForm",views.reviewsform,name="ReviewForm"),
    path("Forget",views.Forget,name="Forget"),
    path("ForgetManage",views.ForgetManage,name="ForgetManage")




]
