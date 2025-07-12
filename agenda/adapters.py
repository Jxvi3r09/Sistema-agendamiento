# agenda/adapters.py
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model

User = get_user_model()

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        print("\n--- Ejecutando pre_social_login ---") # DEBUG
        print(f"Datos recibidos de sociallogin.user: {sociallogin.user.__dict__}") # DEBUG
        print(f"Email del usuario social: {sociallogin.user.email}") # DEBUG

        if sociallogin.user.email: # Asegurarse de que hay un email
            try:
                user = User.objects.get(email=sociallogin.user.email)
                print(f"Usuario existente encontrado por email: {user.email}") # DEBUG
                # Si un usuario existente es encontrado, vincular la cuenta social a él
                sociallogin.connect(request, user)
                print(f"Cuenta social conectada a usuario existente: {user.email}") # DEBUG
            except User.DoesNotExist:
                print(f"No se encontró usuario existente para el email: {sociallogin.user.email}") # DEBUG
                # allauth intentará el auto-signup si SOCIALACCOUNT_AUTO_SIGNUP es True
        else:
            print("¡ADVERTENCIA! El email del usuario social es nulo o vacío.") # DEBUG
        print("--- Fin de pre_social_login ---") # DEBUG