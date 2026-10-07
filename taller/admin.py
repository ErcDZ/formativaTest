from django.contrib import admin
from taller.models import Cliente, Reparacion

class clienteAdmin(admin.ModelAdmin):
    list_display = ["nombre", "fecha_ingreso"]

admin.site.register(Cliente, clienteAdmin)
admin.site.register(Reparacion)