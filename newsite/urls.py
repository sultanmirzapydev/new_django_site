"""newsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('weather/', include('weather.urls')),
    path('bloglistview/', include('blog.urls')),
   # path('register/', include('users.urls')),

    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),

    path('auth/', TemplateView.as_view(template_name="users/auth.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

