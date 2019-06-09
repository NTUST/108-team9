"""foodproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings  # 这一行需要引入
from django.conf.urls.static import static  # 这一行需要引入
from store_list.views import store_showpost
from index import views
from django.views.generic.base import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('origin/', include("origin.urls")),
    path('store_list/', include("store_list.urls")),
    path('store_list/<str:name>/',store_showpost),
    path('history/', include("history.urls")),
    path('concept/', include("concept.urls")),
    path('index/',views.Index),
    path('signin/',views.toSignin),
    path('signup/',views.toSignup),
    path('rank/',views.toRank),
    path('origin/',views.toOrigin),
    path('about_us/',views.toAbout_us),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('', TemplateView.as_view(template_name='index.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
