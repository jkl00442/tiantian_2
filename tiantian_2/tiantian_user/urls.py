from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),

    url(r'^register/$', views.register),
    url(r'^handle_name/$', views.handle_name),
    url(r'^handle_register/$', views.handle_register),
    url(r'^login/$', views.login),
    url(r'^handle_login/$', views.handle_login),
    url(r'^order/$', views.order),
    url(r'^site/$', views.site),
    url(r'^handle_recv/$', views.handle_recv),
    url(r'^logout/$', views.logout),
]
