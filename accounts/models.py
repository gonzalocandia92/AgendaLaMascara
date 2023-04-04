from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Perfil de usuario
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    image = models.ImageField(default='profile_default.png', upload_to='users/', verbose_name='Imagen de perfil')
    address = models.CharField(max_length=150, blank=True, null=True, verbose_name='Dirección')
    location = models.CharField(max_length=150, blank=True, null=True, verbose_name='Localidad')
    telephone = models.CharField(max_length=50, blank=True, null=True, verbose_name='Teléfono')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id']
        
    def __str__(self):
        return self.user.username


# Conexión del Usuario con la extensión de su tabla, el modelo Profile
def created_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(created_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)