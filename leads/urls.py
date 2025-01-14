from django.urls import re_path as url
from leads import views as views
urlpatterns = [
    url(r'^(?P<view_type>|all|watch_later|stopped_watching|upcoming||)$', views.home),
    url(r'^add_lead', views.add_lead),
    url(r'^edit_lead', views.edit_lead),
    url(r'^login', views.login_view),
    url(r'^logout',views.user_logout),
    url(r'^user_action',views.user_action),
    url(r'^user_register',views.user_register),
]