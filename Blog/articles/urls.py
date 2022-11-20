from django.urls import path
from .views import article_list, article_details, user_login, register
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('articles/', article_list, name = 'article_list'),
    path('articles/<slug:slug>/', article_details, name = 'article_details'),
    #path('login/', user_login, name = 'login'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('register/', register, name = 'register'),
    path('password-change/', PasswordChangeView.as_view(), name = 'password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name = 'password_change_done')
]
