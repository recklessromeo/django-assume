from django.conf.urls import *


urlpatterns = patterns('',

    url(r'^auth/user/(\d+)/assume/$', 'assume.views.assume_user', name='assume_user'),

)
