from django.conf.urls import include, url
#from django.contrib import admin
from altadmin.admin import alt_admin



urlpatterns = [
 #   url(r'^admin/', include(admin.site.urls)),
    url('r^admin/', include(alt_admin.urls))
]
