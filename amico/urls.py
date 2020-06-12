"""amico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings  # permite buscar dados do settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('logout/', include('paciente.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),

    # path('', include('paciente.urls')),  # inclui a url da aplicação paciente
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # importado do sttings, ira trazer os valores de midia


admin.site.site_header = 'Amico'
admin.site.site_title = 'Gestão de Atendimentos'
admin.site.index_title = 'Gestão de Atendimentos.'