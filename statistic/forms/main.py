from django.db.models import fields
from django.forms import ModelForm, widgets
from statistic.models import *
from django import forms
from statistic.forms.function import *
class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = {'name', 'date_bday'}
        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_bday': DateBirthday,    # forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Ism Familiya',
            'date_bday': 'Tug\'ilgan sana'
    

        }
    field_order = ['name', 'date_bday']

class StanokForm(ModelForm):
    class Meta:
        model = Stanok
        fields = {'title', 'number', 'workers', 'norma_value'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'workers': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'norma_value': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        labels = {
            'title': 'Nomi',
            'number': 'Nechinchi',
            'workers': 'Tegishli xodimlar',
            'norma_value': 'Norma atqi',
            'organization': 'Zavod'
        }
    field_order = {'title', 'number', 'workers', 'norma_value'}

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = {'date', 'stanok', 'value', 'value2', 'value3'}
        required = {
            'value': True,
            'value2': True,
            'value3': True,
        }
        widgets = {
            'date': DateReport,
            'stanok': forms.Select(attrs={'class': 'form-control'}), 
            'value': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'shift': forms.Select(attrs={'class': 'form-control'}, choices=[('1', '1'), ('2', '2'), ('3', '3')]),
            'value2': forms.NumberInput(attrs={'class': 'form-control'}),
            'value3': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'date': 'Sana',
            'stanok': 'Stanok', 
            'value': 'Atqi 1-smena',
            'value2': 'Atqi 2-smena',
            'value3': 'Atqi 3-smena',
            
        }
    field_order = ['date', 'stanok', 'value', 'value2', 'value3']


class SmenaForm(ModelForm):
    class Meta:
        model = Smena
        fields = {'no', 'master', 'norma_lenta', 'norma_kley', 'organization'}
        required = {
            'no': True,
            'master': True, 
            'norma_lenta': True, 
            'norma_kley': True,
        }

        widgets = {
            'no': forms.NumberInput(attrs={'class': 'form-control'}),
            'master': forms.TextInput(attrs={'class': 'form-control'}),
            'norma_lenta': forms.NumberInput(attrs={'class': 'form-control'}),
            'norma_kley': forms.NumberInput(attrs={'class': 'form-control'}),
            'organization': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'no': '№',
            'master': 'Master', 
            'organization': 'Tashkilot', 
            'norma_lenta': 'Norma lenta', 
            'norma_kley': 'Norma kley',
        }
    field_order = ['no', 'master', 'organization', 'norma_lenta', 'norma_kley']


class SurfaceForm(ModelForm):
    class Meta:
        model = Surface
        fields = {'date', 'smena', 'soni', 'sklad', 'lenta', 'm2', 'kley_st_m2', 'kley_st'}
        widgets = {
            'date': DateReport, 
            'smena': forms.Select(attrs={'class': 'form-control'}),
            'soni': forms.NumberInput(attrs={'class': 'form-control'}),
            'sklad': forms.NumberInput(attrs={'class': 'form-control'}),
            'lenta': forms.NumberInput(attrs={'class': 'form-control'}),
            'm2': forms.NumberInput(attrs={'class': 'form-control'}),
            'kley_st_m2': forms.NumberInput(attrs={'class': 'form-control'}),
            'kley_st': forms.NumberInput(attrs={'class': 'form-control'})
        }

        labels = {
            'date': 'Sana',
            'smena': 'Smena',
            'soni': 'Soni',
            'sklad': 'Sklad M2',
            'lenta': 'Lenta soati',
            'm2': 'M2 soatiga',
            'kley_st_m2': 'Kley st M2',
            'kley_st': 'Kley st soati',
        }
    field_order = ['date', 'smena', 'soni', 'sklad', 'lenta', 'm2', 'kley_st_m2', 'kley_st']