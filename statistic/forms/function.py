from django.db.models import fields
from django.forms import ModelForm, widgets
from statistic.models import *
from django import forms
from datetime import date

class DateBirthday(forms.MultiWidget):
    def __init__(self, attrs=None):
        
        days = [(day, day) for day in range(1, 32)]
        days.insert(0, ('.....', '....'))
        months = [('....', '....'), (1, 'Январь'), (2, 'Февраль'), (3, 'Март'), (4, 'Апрель'), (5,'Май'), (6, 'Июнь'), (7, 'Июль'), (8, 'Август'), (9, 'Сентябрь'), (10, 'Октябрь'), (11, 'Ноябрь'), (12, 'Декабрь')]

        years = [(year, year) for year in range(1920, 2022)]
        years.insert(0, ('....', '...'))
        widgets = [
            forms.Select(attrs={'class': 'form-control date-day',}, choices=days),
            forms.Select(attrs={'class': 'form-control date-month',}, choices=months),
            forms.Select(attrs={'class': 'form-control date-year',}, choices=years),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if isinstance(value, date):
            return [value.day, value.month, value.year]
        elif isinstance(value, str):
            if value[0] == '-':
                year, month, day = ['...', '...', '...']    
            else:
                year, month, day = value.split('-')

            return [day, month, year]
        return [None, None, None]

    def value_from_datadict(self, data, files, name):
        day, month, year = super().value_from_datadict(data, files, name)
        # DateField expects a single string that it can parse into a date.
        return '{}-{}-{}'.format(year, month, day)  




class DateReport(forms.MultiWidget):
    def __init__(self, attrs=None):
        
        days = [(day, day) for day in range(1, 32)]
        days.insert(0, ('.....', '....'))
        months = [('....', '....'), (1, 'Январь'), (2, 'Февраль'), (3, 'Март'), (4, 'Апрель'), (5,'Май'), (6, 'Июнь'), (7, 'Июль'), (8, 'Август'), (9, 'Сентябрь'), (10, 'Октябрь'), (11, 'Ноябрь'), (12, 'Декабрь')]

        years = [(year, year) for year in range(2019, 2040)]
        years.insert(0, ('....', '...'))
        widgets = [
            forms.Select(attrs={'class': 'form-control date-day',}, choices=days),
            forms.Select(attrs={'class': 'form-control date-month',}, choices=months),
            forms.Select(attrs={'class': 'form-control date-year',}, choices=years),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if isinstance(value, date):
            return [value.day, value.month, value.year]
        elif isinstance(value, str):
            if value[0] == '-':
                year, month, day = ['...', '...', '...']    
            else:
                year, month, day = value.split('-')

            return [day, month, year]
        return [None, None, None]

    def value_from_datadict(self, data, files, name):
        day, month, year = super().value_from_datadict(data, files, name)
        # DateField expects a single string that it can parse into a date.
        return '{}-{}-{}'.format(year, month, day)    
