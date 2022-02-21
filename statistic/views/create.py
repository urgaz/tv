from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from statistic.forms.main import *
from statistic.models import *

class WorkerCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create/create_worker.html'
    form_class = WorkerForm
    success_url = '/workers/all'
    




class StanokCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create/create_stanok.html'
    form_class = StanokForm
    success_url = '/tools/all'



class ReportCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create/create_report.html'
    form_class = ReportForm
    success_url = '/reports/all/Jami/0/0/0/'


class SmenaCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create/create_smena.html'
    form_class = SmenaForm
    success_url = '/smena/all'

class SurfaceCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create/create_surface.html'
    form_class = SurfaceForm
    success_url = '/surface/all'
