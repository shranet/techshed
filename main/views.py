from django.shortcuts import render
from django.views.generic import TemplateView

from main.models import TopCategory


class MainIndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        top = [row for row in TopCategory.objects.filter(status=TopCategory.STATUS_ACTIVE).order_by('?').all()[:2]]
        if len(top) == 1:
            top.append(top[0])

        context['top_categories'] = top
        return context


class MainAboutView(TemplateView):
    template_name = 'main/about.html'


class MainContactView(TemplateView):
    template_name = 'main/contact.html'
