# agenda/urls.py


from django.urls import include, path
from . import views
# from .views import login_microsoft_directo

urlpatterns = [
    # path('', login_microsoft_directo),

    path('dashboard/', views.dashboard_view, name='dashboard'),  # Ruta para el dashboard después de iniciar sesión
    
    path('accounts/', include('allauth.urls')),  
    
    path('instructor/', views.instructor, name='instructor'),

    path('coordinador/', views.coordinador, name='coordinador'),

    path('agendador/', views.agendador, name='agendador'),
]
