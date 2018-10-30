from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^user/([0-9]*)$', views.ss_user, name='index'),
    url(r'^user/all', views.all_users),
    url(r'^user/disable/([0-9]*)$', views.disable_user),
    url(r'^user/enable/([0-9]*)$', views.enable_user),
]

