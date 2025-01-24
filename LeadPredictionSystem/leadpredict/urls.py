from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('predict/', views.predict, name='predict'),  # Lead prediction form and result
    path('display_table/', views.display_table, name='display_table'),  # Display saved data
    path('dashboard/', views.dashboard, name='dashboard'),
    path('download/pdf/', views.download_pdf, name='download_pdf'),
    path('download/excel/', views.download_excel, name='download_excel'),
    path('download/word/', views.download_word, name='download_word'),
    path('download/json/', views.download_json, name='download_json'),
]
