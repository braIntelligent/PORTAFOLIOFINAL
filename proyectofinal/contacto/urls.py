from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.contact_view, name='formulario'),
    path('success/', views.mensaje_enviado, name='mensaje_enviado')
]