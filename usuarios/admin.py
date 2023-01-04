from django.contrib import admin
from usuarios.models import Municipio, Departamento, Categoria, Artesano, cliente

admin.site.site_header = 'Administracion ASOARTE STORE'

class AdminClientes(admin.ModelAdmin):
    list_display = ["cod_cliente", "nombre"]
    search_fields = ["cod_cliente"]
    class Meta:
        model = cliente

class AdminMunicipios(admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]
    class Meta:
        model = Municipio

class AdminDepartamento(admin.ModelAdmin):
    list_display = ["nombre_departamento"]
    search_fields = ["nombre_departamento"]
    class Meta:
        model = Departamento


class AdminCategoria(admin.ModelAdmin):
	list_display = ["nombre"]
	search_fields = ["nombre"]
	class Meta:
		model = Categoria

class AdminArtesano(admin.ModelAdmin):
    list_display = ["nombre"]    
    class Meta:
        model = Artesano

admin.site.register(Artesano, AdminArtesano)
admin.site.register(cliente, AdminClientes)
admin.site.register(Categoria, AdminCategoria)
admin.site.register(Municipio, AdminMunicipios)
admin.site.register(Departamento, AdminDepartamento)