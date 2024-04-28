from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('accounts/signup/', views.signup, name='signup'),

    path('dietitians/', views.dietitians_index, name="index"),

    path('dietitians/signup_request_confirmed', views.signup_request_confirmed, name='signup_request_confirmed'),
    path('dietitians/pending_requests', views.pending_requests, name='pending_requests'),
    path('dietitians/approve/<int:dietitian_id>/', views.approve_dietitian, name="approve_dietitian"),
    path('dietitians/delete/<int:dietitian_id>/', views.delete_request, name="delete_request"),

    path('practice/', views.PracticeList.as_view(), name='practice_list'),
    path('practice/create/', views.PracticeCreate.as_view(), name='practice_create'),
]