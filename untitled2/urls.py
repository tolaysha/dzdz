"""untitled2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from myapp.views import *
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main', MainListView.as_view(), name='main'),
    url(r'^^$',  MainListView.as_view(), name='main'),
    url(r'^Bands', BandsListView.as_view(), name='Bands'),
    url(r'^ConcertAgency/', ConcertAgencyListView.as_view(), name='concertAgency'),
    url(r'^about/', about, name='about'),
    url(r'^notification/', notification, name='notification'),
    url(r'^username/', userinfo, name='userinfo'),
    url(r'^registration/', Registration.as_view(), name='registration'),
    url(r'^authorization/', Authorization.as_view(), name='authorization'),
    url(r'^reg2/', registration2, name='reg2'),
    url(r'^logout/', logout, name='logout_url'),



]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
