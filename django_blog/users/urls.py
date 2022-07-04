from django.conf.urls import url
from . import views

app_name = 'users'


urlpatterns = [
    url('signup/', views.signup, name='signup'),
    url('login/', views.login, name='login'),
    url('logout/', views.logout, name='logout'),
]
