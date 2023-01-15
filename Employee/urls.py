from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_page'),
    path('complete-signup/<str:personal_id>/',views.CompleteRegistrationView.as_view(), name='complete_signup-page',kwargs = { 'id': 'id'}),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('', views.dashboard, name='dashboard_page'),

]
