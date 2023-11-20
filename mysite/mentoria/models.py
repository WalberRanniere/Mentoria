from django.db import models
from django.contrib.auth.models import User

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='alunos')

    def __str__(self):
        return self.user.username

class Formulario(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='formularios')
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='formularios')
    nome = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nome} - {self.aluno}"

class Campo(models.Model):
    TIPOS_CAMPO = [
        ('checkbox', 'Checkbox'),
        ('texto', 'Texto'),
        ('seletor', 'Seletor'),
        ('arquivo', 'Arquivo'),
        # Adicione outros tipos conforme necessário
    ]

    formulario = models.ForeignKey('Formulario', on_delete=models.CASCADE, related_name='campos')
    tipo = models.CharField(max_length=20, choices=TIPOS_CAMPO)
    label = models.CharField(max_length=255)
    valor_padrao = models.CharField(max_length=255, blank=True, null=True)
    opcoes_seletor = models.TextField(blank=True, null=True)  # Use para armazenar opções do seletor

    def __str__(self):
        return f"{self.label} - {self.formulario}"