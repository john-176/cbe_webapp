"""
URL configuration for session_auth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# session_auth/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from session_app.views import FrontendAppView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('session_app.urls')),
    path('api/', include('content_app.urls')),
    path('api/', include('timetable_app.urls')),
    
    # Catch-all for React frontend **after Django routes**
    re_path(r'^(?!admin|api|media|static).*$' , FrontendAppView.as_view(), name='frontend'),
    #re_path(r'^.*$', FrontendAppView.as_view(), name='frontend'),  # Catch all
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
