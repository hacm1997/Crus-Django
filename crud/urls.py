
from django.contrib import admin
from django.urls import path, include
from crud.apps.CrudApp import urls as app_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(app_url))
]
