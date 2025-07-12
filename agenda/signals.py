from django.dispatch import receiver
from allauth.account.signals import user_logged_in
from django.contrib.auth import logout
from django.shortcuts import redirect

# agenda/signals.py
from allauth.account.signals import user_logged_in
from django.dispatch import receiver


## Esta señal se activa cuando un usuario inicia sesión con Microsoft a través de django-allauth
# Esta señal se utiliza para completar los datos del perfil del usuario con la información obtenida de mi
@receiver(user_logged_in)
def populate_user_profile(request, user, **kwargs):
    socialaccount = user.socialaccount_set.first()
    if socialaccount:
        data = socialaccount.extra_data
        user.email = data.get('mail') or data.get('userPrincipalName')
        user.first_name = data.get('givenName', '')
        user.last_name = data.get('surname', '')
        user.save()

