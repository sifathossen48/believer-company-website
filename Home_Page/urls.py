from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='abouts'),
    path('certification/', views.CertificationView.as_view(), name='certification'),
    path('structural-and-safety-compliance/', views.StructuralView.as_view(), name='structural'),
    path('testing-and-inspection/', views.TestingView.as_view(), name='testing'),
    path('others-service/', views.OtherView.as_view(), name='others')
]