"""ielts_vocal_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url

from .views.list import VocalListView
from .views.create import VocalCreate
from .views.detail import DetailView
from .views.list_admin import VocalListAdminView
from .views.detail_admin import DetailAdminView


app_name = 'vocal'

urlpatterns = [
    url(r'^list/$', VocalListView.as_view(), name="vocal_list"),
    url(r'^create/$', VocalCreate.as_view(), name="create_vocal"),
    url(r'^details/(?P<vocal_id>[0-9A-Za-z]+)/$', DetailView.as_view(), name="vocal_detail"),

    url(r'^list_admin/$', VocalListAdminView.as_view(), name="vocal_list_admin"),
    url(r'^details_admin/(?P<vocal_id>[0-9A-Za-z]+)/$', DetailAdminView.as_view(), name="vocal_detail_admin"),


]
