from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
#MVC = Modelo vista controlador -> Acciones (metodos)
#MVT = Modelo Template Vista -> Acciones (metodos)

layout = """
<h1>Sitio web con Django | Rafael Galvez </h1>
<hr />

<ul>
    <li>
        <a href="/hola-mundo">Hola mundo</a>
    </li>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Pagina de pruebas</a>
    </li>
    <li>
        <a href="/contacto">Contacto</a>
    </li>
</ul>
<hr />
"""



def index(request):

    html ="""
    <h1>Inicio<h1>
    <p>Año hasta el 2050: </p>
    <ul>
    """
    year = 2021
    while year <= 2030:
        if year % 2 == 0: 
            html += f"<li>{str(year)}</li>"
        year += 1 
    html+="</ul>"
    return HttpResponse(layout+html)


    

def hola_mundo(request): #Request es un parametro que va permitior recibir peticiones a la url
    return HttpResponse(layout+"Hola Mundo con Django")

def pagina(request, redirigir = 0):

    if redirigir == 1: # Redirecciones
        return redirect('contacto', nombre="Rafael",apellidos="Galvez")

    return HttpResponse(layout+"""
    <h1>Pagina de mi web</h1>
    """)


def contacto(request, nombre="",apellidos=""):
    html = ""
    if nombre and apellidos: 
        html += "<p>El nombre completo es:</p>"
        html += f"<h3>{nombre} {apellidos}</h3>"
    return HttpResponse(layout+f"<h2>Contactos</h2>"+html)