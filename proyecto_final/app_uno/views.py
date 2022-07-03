from django.http import HttpResponse
from django.shortcuts import render
from app_uno.models import Avatar, Comida
from app_uno.models import Cocinero
from app_uno.models import Receta
from django.template import loader
from app_uno.forms import Cocinero_formulario, UserEditForm, Comidas_formulario
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    
    return render(request , "inicio.html")


@login_required
def perfil(request):

    usuario = request.user

    if request.method == "POST":

        miFormulario= UserEditForm(request.POST)

        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()
            return render(request , "inicio.html")

    else:
        miFormulario = UserEditForm(initial={'email': usuario.email})
    
    return render(request , "perfil.html" , {"miFormulario": miFormulario , "usuario": usuario})


def comidas(request):
    return render(request , "comidas.html")
  

def cocineros(request):
    cocineros = Cocinero.objects.all()
    dicc = {"cocineros": cocineros }
    plantilla = loader.get_template("cocineros.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

@login_required
def recetas(request):
    return render(request , "recetas.html")


def alta_comida(request , nombre):

    comida = Comida(nombre = nombre , camada = 5624)
    comida.save()

    texto = f"Se guardó en la base de datos la comida: {comida.nombre} y su camada es: {comida.camada}"
    return HttpResponse(texto)

def alta_cocinero(request , nombre):
    
    cocinero = Cocinero(nombre = nombre , camada = 6843)
    cocinero.save()

    texto = f"Se guardó en la base de datos el cocinero: {cocinero.nombre} y su camada es: {cocinero.camada}"
    return HttpResponse(texto)

def contacto(request):
    
    return render(request , "contacto.html")

def portafolio(request):

    return render (request , "portafolio.html")


@login_required
def cocinero_formulario(request):

    if request.method == "POST":

        formulario_uno = Cocinero_formulario(request.POST)
        if formulario_uno.is_valid():
            datos = formulario_uno.cleaned_data

            cocinero = Cocinero(nombre=datos['nombre'] , camada=datos['camada'])
            cocinero.save()
            return render(request , "formulario.html")

    return render(request , "formulario.html")

@login_required
def comidas_formulario(request):

    if request.method == "POST":

        formulario_uno = Comidas_formulario(request.POST)
        if formulario_uno.is_valid():
            datos = formulario_uno.cleaned_data

            comida = Comida(nombre=datos['nombre'] , camada=datos['camada'])
            comida.save()
            return render(request , "formulario_comidas.html")

    return render(request , "formulario_comidas.html")



def buscar_cocinero(request):
    
    return render(request , "buscar_cocinero.html")


def buscar(request):

    if request.GET ['nombre']:
        nombre = request.GET['nombre']
        cocineros = Cocinero.objects.filter(nombre__icontains = nombre)
        return render(request , "resultado_busqueda.html" , {"cocineros":cocineros})

    else:
        return HttpResponse("Campo vacío")


@login_required
def lista_cocineros(request):
    cocineros = Cocinero.objects.all()
    dicc = {"cocineros": cocineros }
    plantilla = loader.get_template("lista_cocineros.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


@login_required
def eliminar_cocinero(request , id):

    cocinero = Cocinero.objects.get(id=id)
    cocinero.delete()


    cocinero = Cocinero.objects.all()
    return render(request , "lista_cocineros.html" , {"cocineros": cocinero})


@login_required
def editar(request , id):
    cocinero = Cocinero.objects.get(id=id)
    if request.method == "POST":

        cocinero_formulario = Cocinero_formulario(request.POST)
        if cocinero_formulario.is_valid():
            datos = cocinero_formulario.cleaned_data
            cocinero.nombre = datos['nombre']
            cocinero.camada = datos ['camada']
            cocinero.save()

            cocinero = Cocinero.objects.all()

            return render(request , "lista_cocineros.html" , {"cocineros": cocinero})
    else:
        cocinero_formulario=Cocinero_formulario(initial={'nombre':cocinero.nombre , 'camada': cocinero.camada})
        return render(request , "editar_cocinero.html" , {"cocinero_formulario": cocinero_formulario , "cocinero":cocinero})
            


def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request , data= request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password= contra)

            if user is not None:
                login(request , user)
                avatares =  Avatar.objects.filter(user=request.user.id)
                return render(request , "inicio.html" , {"url": avatares[0].imagen.url})

                
            
            else:
                return HttpResponse(f"Usuario incorrecto")
        else:
            return HttpResponse(f"Usuario incorrecto {form}")
    


    form = AuthenticationForm()
    return render(request , "login.html" , {"form": form})





def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse( "Usuario creado correctamente")


    else:
        form = UserCreationForm()
    return render (request , "registro.html" , {"form": form})


def about_me(request):
    return render(request , "about_me.html")



















