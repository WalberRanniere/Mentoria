from django.contrib import admin
from .models import Mentor, Aluno, Formulario, Campo

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('user', )  # Adicione outros campos, se necessário

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('user', 'mentor')  # Adicione outros campos, se necessário

@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'aluno', 'nome')  # Adicione outros campos, se necessário

@admin.register(Campo)
class CampoAdmin(admin.ModelAdmin):
    list_display = ('formulario', 'tipo', 'label', 'valor_padrao', 'opcoes_seletor')  # Adicione outros campos, se necessário

