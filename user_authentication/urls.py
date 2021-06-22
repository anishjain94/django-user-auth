from django.urls import path
from user_authentication import views
from django.views.generic import TemplateView


urlpatterns = [
    path('user/', views.user_list),
    path('user/<str:username>/', views.user_detail),
]
