from pipes import Template
from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from app_coder.models import Familiares

def crear_familiar(self):

    today = datetime.today().strftime('%Y-%m-%d')

    # familiar = Familiares(nombre="Juan", apellido="Perez", edad=35, fechaDeCreacion=today)
    # familiar = Familiares(nombre="Pamela", apellido="Lozano", edad=11, fechaDeCreacion=today)
    familiar = Familiares(nombre="Orlando", apellido="Manrriquez", edad=62, fechaDeCreacion=today)

    familiar.save()

    return HttpResponse("Familiar creado correctamente")

def obtener_familiares(self):

    list_family = []
    for familiar in Familiares.objects.all():

        list_family.append({"nombre":familiar.nombre, "apellido": familiar.apellido, "edad":familiar.edad, "fecha":familiar.fechaDeCreacion})

    plantilla = loader.get_template("template.html")

    dict = {"data":list_family}

    documento = plantilla.render(dict)

    return HttpResponse(documento)