from django.urls import path

from user import views


app_name = 'user'

urlpatterns = [
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup')

]
