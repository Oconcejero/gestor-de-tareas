from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect


urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('', lambda request: redirect('login'), name='root'),
    path('admin/', admin.site.urls),
    path('tareas/', include('tareas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
