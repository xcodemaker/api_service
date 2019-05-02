from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from data_reader import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^stateToCode/$',views.getCode),
    url(r'^codeToState/$',views.getState)
]
