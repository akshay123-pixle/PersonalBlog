
from django.contrib import admin
from django.urls import path
from blog.views import index,about,contact,post,comment_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index,name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('post/<int:pk>/',post,name='post'),
    path('post/<int:post_id>/comment/',comment_detail,name='comment'),


]
