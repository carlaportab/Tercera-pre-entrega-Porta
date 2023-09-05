from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
	return HttpResponse("Holaaa")

def probandoTemplate(self):
	
    miHtml = open("C:/Users/Carla Porta/Desktop/MiProyecto/Proyecto1/Proyecto1/templates/template1.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)