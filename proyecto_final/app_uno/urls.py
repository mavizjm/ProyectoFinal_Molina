from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("perfil" , views.perfil, name="perfil"),
    path("about_me" , views.about_me , name="acerca_de_mi"),
    path("" , views.inicio , name="inicio"),
    path("cocineros" , views.cocineros , name="cocineros"),
    path("comidas", views.comidas , name="comidas"),
    path("recetas" , views.recetas, name="recetas"),
    path("alta_comidas/<nombre>" , views.alta_comida),
    path("contacto" , views.contacto , name="contacto"),
    path("portafolio" , views.portafolio , name="portafolio"),
    path("alta_cocinero" , views.cocinero_formulario , name="formulario"),
    path("alta_comidas" , views.comidas_formulario, name="formulario_comidas"),
    path("buscar_cocinero", views.buscar_cocinero),
    path("buscar" , views.buscar , name="buscar"),
    path("lista_cocineros" , views.lista_cocineros , name="lista_cocineros"),
    path("eliminar_cocinero/<int:id>" , views.eliminar_cocinero, name="eliminar_cocinero"),
    path("editar_cocinero/<int:id>" , views.editar , name="editar_cocinero"),
    path("editar_cocinero" , views.editar , name="editar_cocinero"),
    path("login" , views.login_request , name="login"),
    path("register" , views.register , name="registro"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="logout"),




    



]