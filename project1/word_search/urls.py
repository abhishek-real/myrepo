from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home_page,name="home"),
    path('register/',views.register,name="register"),
    path('paragraph/',views.paragraph,name="paragraph"),
    path('search_paragraph/',views.search_paragraph,name="search_paragraph"),
]
