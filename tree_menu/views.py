from django.shortcuts import render
from django.views import View

class MenuView(View):
    template_name = 'tree_menu/menu.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
