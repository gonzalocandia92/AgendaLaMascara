from django.contrib.auth.models import Group
from .models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save


# # Cuando viene una señal de grabar un registro me va a tomar este receive ese evento de grabación
# y lo voy a mandar a esta función, si está creado el usuario tomará el nombre de grupo estudiante sino lo crea.
# Luego lo agrega al estudiante al grupo estudiante

@receiver(post_save, sender=Profile)
def add_user_to_students_group(sender, instance, created, **kwargs):
    if created:
        try:
            visits = Group.objects.get(name='visitante')
        except Group.DoesNotExist:
            visits = Group.objects.create(name='visitante')
            Group.objects.create(name='boleteria')
            Group.objects.create(name='gestor')
            Group.objects.create(name='direccion')
        instance.user.groups.add(visits)
        
        