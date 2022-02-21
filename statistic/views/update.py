from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from statistic.forms.main import *
from statistic.models import *

class StanokEditView(LoginRequiredMixin, UpdateView):
    model = Stanok
    form_class = StanokForm
    success_url = '/tools/all'
    # def get_context_data(self, **kwargs):
    #     print(kwargs)
        
    #     context = super().get_context_data(**kwargs)
    #     print(context['view'].__dict__)
    #     return context

class ReportEditView(LoginRequiredMixin, UpdateView):
    model = Report
    form_class = ReportForm

    
    def get_success_url(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        values = context['view'].__dict__['kwargs']
        return '/reports/all/{}/{}/{}/{}/'.format(values['st'], str(values['year']), str(values['month']), str(values['day']))

class SmenaEditView(LoginRequiredMixin, UpdateView):
    model = Smena
    form_class = SmenaForm
    success_url = '/smena/all'