from django.contrib import admin
from .models import Maquina, Prestamo 

# Registra tus modelos aquí
# Todo esto es totalmente opcional
admin.site.register(Maquina)
admin.site.register(Prestamo)

class MaquinaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'marca', 'modelo', 'numero_serie')  # Campos que quieres mostrar en la lista
    search_fields = ('marca', 'modelo')  # Campos por los que se puede buscar

# Ahora registra el modelo con esta configuración personalizada
admin.site.register(Maquina, MaquinaAdmin)
