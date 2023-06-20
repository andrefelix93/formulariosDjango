from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('formulariohtml', views.formulariohtml, name='formulariohtml'),
    path('processa_formulario_html', views.processa_formulario_html, name='processa_formulario_html'),
    path('formularioforms', views.formularioforms, name='formularioforms'),
    path('processa_formulario_forms', views.processa_formulario_forms, name='processa_formulario_forms'),
    path('formularioModels', views.formularioModels, name='formularioModels'),
    path('processa_formulario_model', views.processa_formulario_model, name='processa_formulario_model'),
]