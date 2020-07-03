
from django.urls import path
from . import views
app_name = "tube"

urlpatterns = [
     path('', views.index , name="index"),
     path('author/<name>', views.getauthor, name="profile"),
     path('article/<int:id>', views.getsingle, name= "Single"),
     path('topic/<name>', views.gettopic, name= "Topic"),
     path('login/', views.getlogin, name= "loging"),
     path('logout/', views.getlogout, name= "logout"),
     path('create/', views.getcreate, name= "Create"),
     path('profile/', views.profile, name= 'profile'),
     path('update/<int:id>', views.update, name='Update'),
     path('Delete/<int:id>', views.delet, name='Delet'),
     path('register/', views.register, name='Register'),
     path('subjects/', views.getsubjects, name="Subject"),
     path('create/topic', views.getcreate_topic, name="create_topic"),

]
     
