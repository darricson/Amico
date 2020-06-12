from django.contrib import admin
from .models import Paciente, Empresa, Exame, Atendimento, Laboratorio


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'empresa', 'funcao', )
    list_filter = ('empresa',)
    search_fields = ('rg',)


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cnpj',)
    search_fields = ('cnpj',)


class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')


class ExameAdmin(admin.ModelAdmin):
    list_display = ('nome', 'laboratorio',)


class AtendimentoAdmin(admin.ModelAdmin):
    list_filter = ('exames',)
    list_display = ('paciente', 'get_exame', 'dd_atendimento')

#  esta função permiti adicionar campos many tomany no listdisplay
    def get_exame(self, obj):
        return ', '.join([e.nome for e in obj.exames.all()])
    get_exame.short_description = 'Exames'


#  Register your models here.
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(Exame, ExameAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Atendimento, AtendimentoAdmin)
