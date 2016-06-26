from django.conf.urls import include, url

"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from jurblog import views

urlpatterns = [
    # indexes
    url(r'^$',views.index, name='index'),
    url(r'^category/(?P<slug>[-\w]+)/$', views.category, name='category'),
    #url(r'^$', views.home, name='home')
    # archives
    url(r'^archive/(?P<year>\d{4})/$', views.archive_year, name='archive_year'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', views.archive_month, name='archive_month'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', views.archive_day, name='archive_day'),

    # details
    url(r'^details/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.details, name='details'),
]
