from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexVew.as_view(),name='home'),
    path('reports/',views.ReportView.as_view(),name='reports')
]