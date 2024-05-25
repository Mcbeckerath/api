from django.urls import path
from app import views

urlpatterns = [
    path('relacao/', views.relacao),    
    path('relacao/<id>', views.relacao_id),    
]