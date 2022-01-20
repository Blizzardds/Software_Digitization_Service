from django.urls import path
from django.contrib.auth import views as auth_views
from userAccount import views
from userAccount.models import User 

urlpatterns = [

    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name="profile"),
    


    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="../templates/password_reset.html"), name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="../templates/password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="../templates/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="../templates/password_reset_done.html"), name='password_reset_complete')
]
