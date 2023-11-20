from django.shortcuts import render
from django.views import View, generic


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render (request, 'mentoria/index.html',)
