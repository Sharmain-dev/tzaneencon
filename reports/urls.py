from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_report, name='create_report'),
    path('success/<str:reference_number>/', views.report_success, name='report_success'),
    path('track/', views.track_report, name='track_report'),  
]