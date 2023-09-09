from . import views
from django.urls import path

urlpatterns = [
    path('models/', views.CarModelView.as_view(), name='car-models'),
    path('models/<int:pk>/', views.CarModelView.as_view(), name='car-models'),
    path('all/', views.CarView.as_view(), name='car-list'),
    path('<int:pk>/', views.CarView.as_view(), name='car-detail'), 
    path('appuser/', views.AppUserView.as_view(), name='app-user'),
    path('appuser/<int:pk>/', views.AppUserView.as_view(), name='app-user'),
    path('userprof/', views.UserProfileView.as_view(), name='app-user'),
    path('userprof/<int:pk>/', views.UserProfileView.as_view(), name='app-user'),
    path('ad/', views.AdView.as_view(), name='app-user'),
    path('ad/<int:pk>/', views.AdView.as_view(), name='app-user'),

]