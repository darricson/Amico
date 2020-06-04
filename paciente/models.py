from django.db import models

class Paciente(models.Model):
    nome = models.CharField('Nome', max_length=100, blank=False)
    funcao = models.CharField('Função', max_length=50)
    data_nasc = models.DateField('Data nascimento')
    rg = models.IntegerField('RG', max_length=15, blank=False)
    orgao_exp = models.CharField('Orgão Expedidor', max_length=5, blank=False)

    def__str__(self):
        return self.nome


class Endereco(models.Model):

    estados = [
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

    rua = models.CharField('Rua/Av./Logradouro', max_length=80)
    numero = models.CharField('Numero/Bloco/Quadra', max_length=50)
    bairro = models.CharField('Bairro', max_length=50)
    cidade = models.CharField('Cidade', max_length=80)
    estado = models.CharField('Estado', max_length=5, choices=estados)

    def__str__(self):
        return self.bairro

class Empresa(models.Model):
    nome = models.CharField('Nome', max_length=80, blank=False)
    email = models.EmailField('E-mail',max_length=100)
    cnpj = models.CharField('CNPJ', max_length=11)

    def__str__(self):
        return self.nome


class Exame(models.Model):
    nome = models.CharField('Exame', max_length=50)
