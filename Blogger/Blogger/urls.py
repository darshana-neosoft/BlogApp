"""Blogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
import bloggerapp
from django.conf.urls.static import static
from Blogger import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$','bloggerapp.views.index',name="index"),
    url(r'^signup-page/', 'bloggerapp.views.signup_page',name="signup_page"),
    url(r'^blog-page/', 'bloggerapp.views.blog_page',name="blog_page"),
    url(r'^user-login/', 'bloggerapp.views.user_login',name="user_login"),
    url(r'^user-signup/', 'bloggerapp.views.user_signup',name="user_signup"),
    url(r'^add-blog/', 'bloggerapp.views.add_blog',name="add_blog"),
    url(r'^add-blog-like/', 'bloggerapp.views.add_blog_like',name="add_blog_like"),
    url(r'^blog-details/', 'bloggerapp.views.blog_details',name="blog_details"),
    url(r'^add-blog-comment/', 'bloggerapp.views.add_blog_comment',name="add_blog_comment"),
    url(r'^log-out/', 'bloggerapp.views.log_out',name="log_out"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


