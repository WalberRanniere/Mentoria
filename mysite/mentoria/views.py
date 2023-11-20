from django.shortcuts import render
from django.views import View, generic

from .models import Mentor, Aluno, Formulario, Campo

class IndexView(View):
    def get(self, request, *args, **kwargs):
        mentor = Mentor.objects.first()
        alunos = Aluno.objects.filter(mentor = request.user.mentor)
        contexto = {'mentor': mentor, 'lista_alunos': alunos}
        return render (request, 'mentoria/index.html', contexto)
