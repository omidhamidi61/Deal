from django.conf.urls import url
from app1 import views
app_name='app1'
urlpatterns = [
    url('login/',views.login,name = 'login'),
    url('ajcheckusername',views.checkusername,name = 'checkusername'),
    url('ajcheckpassword',views.checkpassword,name = 'checkpassword'),

    url('home/',views.home,name = 'home'),
    url('inbox/', views.inbox,name = "inbox"),
    url('outbox/', views.outbox,name = "outbox"),
    
    url('unreadmessages/', views.unreadmessages,name = 'unreadmessages'),
    url('ajchecksendermails', views.checksendermails, name = 'checksendermails'),
    url('ajcheckreceivermails', views.checkreceivermails, name = 'ajcheckreceivermails'),
    url('ajshowcontent/',views.showcontent, name = 'showcontent'),
    url('ajdeal/',views.deal, name = 'ajdeal'),
    
    ]