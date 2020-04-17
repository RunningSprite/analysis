from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'user/$', views.user, ),
    url(r'^upload_excel/$', views.upload_excel),
    url(r'^handle_word_txt/$', views.handle_word_txt),
    # url(r'^user/(?P<pk>[0-9]+)/$', views.user),
    # url(r'^user/', views.user),
    # url(r'^upload_csv/', views.upload_csv()),
    # url(r'^delete_user/', views.delete_user()),
]