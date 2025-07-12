from django.shortcuts import render
from django.shortcuts import redirect
import urllib.parse
from django.contrib.auth.decorators import login_required

# Create your views here.
# Esta vista redirige al usuario a la página de inicio de sesión de Microsoft
# Utiliza la biblioteca urllib.parse para construir la URL de redirección con los parámetros necesarios

# Esta vista renderiza la plantilla de inicio de sesión
# La plantilla debe contener un enlace al inicio de sesión de Microsoft
def login_view(request):
    return render(request, 'login.html')

@login_required
def dashboard_view(request):
    # Aquí puedes agregar la lógica para mostrar el dashboard después de iniciar sesión
    return render(request, 'dashboard.html')

from django.shortcuts import render

def instructor(request):
    return render(request, 'roles/instructor.html')

def coordinador(request):
    return render(request, 'roles/coordinador.html')

def agendador(request):
    return render(request, 'roles/agendador.html')
