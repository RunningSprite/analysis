from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'user/$', views.user, ),
    url(r'^user_list/$', views.user_list),
    # url(r'^user/(?P<pk>[0-9]+)/$', views.user),
    # url(r'^user/', views.user),
    url(r'^delete_user/', views.user),
    # url(r'^delete_user/', views.delete_user()),
]