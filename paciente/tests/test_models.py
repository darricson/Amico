from django.test import TestCase
from model_mommy import mommy


class EmpresaTestCase(TestCase):
    def setUp(self):
        self.empresa = mommy.make('Empresa')

    def test_str(self):
        self.assertEqual(str(self.empresa), self.empresa.nome)


class PacienteTestCase(TestCase):

    def setUp(self):
        self.paciente = mommy.make('Paciente')

    def test_paciente(self):
        self.assertEqual(str(self.paciente), self.paciente.nome)


class LabotatorioTestCase(TestCase):

    def setUp(self):
        self.laboratorio = mommy.make('Laboratorio')

    def test_laboratorio(self):
        self.assertEqual(str(self.laboratorio), self.laboratorio.nome)


class ExameTestCase(TestCase):

    def setUp(self):
        self.exame = mommy.make('Exame')

    def test_exame(self):
        self.assertEqual(str(self.exame), self.exame.nome)


class AtendimentoTestCase(TestCase):

    def setUp(self):
        self.atendimento = mommy.make('Atendimento')

    def test_atendimento(self):
        self.assertEqual(str(self.atendimento), f'{self.atendimento.paciente}')
