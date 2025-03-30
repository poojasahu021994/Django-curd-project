from django.urls import path
from .import views

urlpatterns=[
    path ('', views.index,name='index'),
    path ('login/', views.login,name='login'),
    path ('Registration/', views.Registration,name='Registration'),
    path ('admindashboard/', views.admindashboard,name='admindashboard'),
    path ('userdashboard/<int:pk>', views.UserDashbashboard,name='userdashboard'),
    path('profile/<int:pk>/',views.profile, name='profile'),
    path('addtask/',views.Addtask, name='addtask'),
    path('givetask/<int:pk>',views.givetask,name='givetask'),
    path('remove/<int:pk>',views.remove,name='remove'),
    path('logout/',views.Logout,name='logout'),
    path('showtask/',views.Showtask, name='showtask'),
    path('usertask/<int:pk>/',views.usertask, name='usertask'),
    path('edituser/<int:pk>/',views.edituser, name='edituser'),
    path('updatedata/<int:pk>/',views.updatedata,name='updatedata'),
    path('update/<int:pk>/',views.update,name='update'),




]