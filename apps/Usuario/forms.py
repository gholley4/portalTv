from django.contrib.auth.models import User
from django.contrib.auth.models import UserCreationForm

class RegistroForm(UserCreationForm)

    class meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
        ]

        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo',
        }