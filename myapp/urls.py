from django.urls import path
from myapp.views import *


urlpatterns = [
    path('', index, name='index'), 
    path('all_events/', all_events, name='all_events'), 
    path('add_event/', add_event, name='add_event'), 
    path('crear_event', crear_event, name='crear_event'),
    path('update/', update, name='update'),
    path('remove/<int:id>', remove, name='remove'),
    path('actualizar_event/<int:id>', actualizar_event, name='actualizar_event'),
]