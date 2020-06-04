from django.contrib import admin
from .models import Paciente, Empresa, Exame, Endereco

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Endereco)
admin.site.register(Exame)
admin.site.register(Empresa)