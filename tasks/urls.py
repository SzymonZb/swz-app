from django.urls import path
from tasks import views


urlpatterns = [
    path('', views.home, name="home"),
    path('tasks/', views.tasks, name='tasks'),
    path('employee/<str:pk_test>/', views.employee, name='employee'),
    path('update_task/', views.updateTask, name='update_task'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.userPage, name='userPage'),
    path('overview/<str:pk_ov>/', views.overview, name='overview')
]
