from django.contrib import admin
from Api_Proyecto.models import Inscritos
from Api_Proyecto.models import Institucion
# Register your models here.

class InscritosAdmin(admin.ModelAdmin):
    list_display = ['nombre']

admin.site.register(Inscritos, InscritosAdmin)

class InstitucionAdmin(admin.ModelAdmin):
    list_display = ['institucion']

admin.site.register(Institucion, InstitucionAdmin)
