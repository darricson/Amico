from django.contrib import admin
from .models import Paciente, Empresa, Exame, Atendimento


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'empresa', 'funcao', )
    list_filter = ('empresa',)
    search_fields = ('rg',)


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cnpj',)
    search_fields = ('cnpj',)


class ExameAdmin(admin.ModelAdmin):
    list_display = ('nome', 'laboratorio',)


class AtendimentoAdmin(admin.ModelAdmin):
    list_filter = ('exame',)
    list_display = ('paciente', 'dd_atendimento',)



# Register your models here.
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Exame, ExameAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Atendimento, AtendimentoAdmin)
