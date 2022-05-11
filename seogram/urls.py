"""seogram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from about.views import about
from account.views import register, auth, logout_user
from service.views import service
from blog.views import blog, blog_details
from main.views import main_page
from django.conf.urls.static import static
from . import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('about/', about, name='about'),
                  path('', main_page, name='home'),
                  path('service/', service, name='service'),
                  path('blog/', blog, name='blog'),
                  path('blog/<int:key>', blog_details, name="detail"),
                  path('register', register, name='register'),
                  path('login', auth, name='login'),
                  path('logout', logout_user, name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
