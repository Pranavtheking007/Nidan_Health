"""nidantrial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
'''from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',)
]'''


from django.contrib import admin
from base import views
from django.urls import path,include


urlpatterns = [
    #path('admin/',admin.site.urls),
    path('',include('base.urls')),
    #path('^$',include('base.urls')),
    path('Login', include('base.urls')),
    path('SignUP',include('base.urls')),
    path('index.html',include('base.urls')),
    path('stroke.html',include('base.urls')),
    path('heartdisease.html',include('base.urls')),
    path('card.html',include('base.urls')),
    path('diabetes.html',include('base.urls')),
    path('diabetesmed.html',include('base.urls')),
    path('mentalhealthstudents.html',include('base.urls')),
    path('Result_Tp.html',include('base.urls')),
    path('chronicdiseaseabout.html',include('base.urls')),
    path('physicalhealthabout.html',include('base.urls')),
    path('mentalhealthabout.html',include('base.urls')),
    path('dashboardindex.html',include('base.urls')),

]




