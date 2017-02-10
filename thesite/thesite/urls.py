"""thesite URL Configuration

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

from django.conf.urls import include, url
from django.contrib import admin

from filebrowser.sites import site
from django.contrib.auth import views as auth_views

from django.conf.urls.i18n import i18n_patterns
 



from accalascio import views

urlpatterns = [
    # url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
    #     views.home, name='home'),
]

urlpatterns += i18n_patterns(
    url(r'^$', views.home, name='home'),
    url(r'^contatti', views.contatti, name='contatti'),
    url(r'^montagna/', views.montagna, name='montagna'),
    url(r'^affitto/', views.affitto, name='affitto'),
    url(r'^eventi/', views.eventi, name='eventi'),
    url(r'^accalascio/', views.accalascio, name='accalascio'),
    url(r'^book/(\d+)/$',  views.book, name='book'), 
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),    
    url(r'^grappelli/', include('grappelli.urls')), 
    url(r'^admin/', admin.site.urls),
    url('^accounts/login/$', auth_views.login)
)


