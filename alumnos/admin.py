from django.contrib import admin
from .models import cliente,Registro_cliente,BoletaModel,Categoria, Articulo,detalle_boleta,Boleta,Productos

# Register your models here.
admin.site.register(cliente)
admin.site.register(Registro_cliente)
admin.site.register(BoletaModel)
admin.site.register(Categoria)
admin.site.register(Articulo)
admin.site.register(detalle_boleta)
admin.site.register(Boleta)
admin.site.register(Productos)