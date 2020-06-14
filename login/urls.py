from django.conf.urls import url 
from .views import loginView,logoutView

app_name = 'login'

urlpatterns = [
    
    url(r'^$', loginView, name="login"),
	url(r'^logout/$', logoutView, name="logout")
]



