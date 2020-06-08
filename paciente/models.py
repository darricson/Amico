from django.db import models
import datetime


class Empresa(models.Model):
    nome = models.CharField(max_length=80, blank=False, verbose_name='Nome')
    email = models.EmailField(max_length=100, verbose_name='E-mail')
    cnpj = models.CharField(max_length=11, unique=True, verbose_name='CNPJ')

    def __str__(self):
        return self.nome


class Paciente(models.Model):
    estates = [

        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espirito Santo'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MTS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondonia'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),

    ]

    sex = [

        ('m', 'masculino'),
        ('f', 'feminino'),
        ('o', 'outros'),
    ]

    nome = models.CharField(max_length=100, blank=False, verbose_name='Nome')
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, verbose_name='Epresa')
    funcao = models.CharField(max_length=50, verbose_name='Função')
    sexo = models.CharField(max_length=2, choices=sex, verbose_name='Sexo')
    data_nasc = models.DateField(verbose_name='Data nascimento')
    rg = models.IntegerField('RG', blank=False, unique=True)
    orgao_exp = models.CharField(max_length=5, blank=False, verbose_name='Orgão Expedidor')
    telefone = models.CharField(max_length=12, verbose_name='Telefone')
    rua = models.CharField(max_length=80, verbose_name='Rua/Av./Logradouro')
    numero = models.CharField(max_length=50, verbose_name='Numero/Bloco/Quadra')
    bairro = models.CharField(max_length=50, verbose_name='Bairro')
    cidade = models.CharField(max_length=80, verbose_name='Cidade')
    estado = models.CharField(max_length=10, choices=estates, verbose_name='Estado')

    def __str__(self):
        return self.nome


class Exame(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Exame')
    laboratorio = models.CharField(max_length=60, verbose_name='Laboratorio / Empresa')

    def __str__(self):
        return self.nome


class Atendimento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name='Paciente')
    exame = models.ManyToManyField(Exame, verbose_name='Exame')
    observacao = models.TextField(max_length=500, blank=True, verbose_name='Observações')
    dd_atendimento = models.DateTimeField(auto_now=True, verbose_name='Data de atendimento')


