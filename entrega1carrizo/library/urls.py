from re import template
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token
from .views import FormView, SearchView

app_name = "library"
urlpatterns = [
    path('form/', FormView.as_view(), name='formulario'),
    path('search/', SearchView.as_view(),name='search'),    
]
