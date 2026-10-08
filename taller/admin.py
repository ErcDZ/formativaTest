from django.contrib import admin
from taller.models import Cliente, Reparacion

class clienteAdmin(admin.ModelAdmin):
    list_display = ["nombre", "fecha_ingreso"]

class reparacionAdmin(admin.ModelAdmin):
    list_display = ["nombre_coche", "descripcion", "fecha_registrado", "monto"]
    list_filter = ["monto"]
    search_fields = ["fecha_registrado"]

admin.site.register(Cliente, clienteAdmin)
admin.site.register(Reparacion, reparacionAdmin)