from django.urls import path

from . import views



urlpatterns = [
    path('allpost', views.home, name= "allpost"),
    path('home', views.categorypost, name= "home"),
    path('', views.categorypost, name= "home"),
    path('category/<str:cats>', views.CategoryView, name= "category"),
    path("post/<id>", views.post_detail , name="post_detail"),
    path("search", views.search , name="search"),
    path("author", views.authorview , name="author"),
    path("logout", views.logout_view , name="logout"),
    path("login", views.login_view , name="login"),
    path("aboutus", views.aboutusview , name="aboutus"),
    path("mail", views.mail_view , name="mail"),
]