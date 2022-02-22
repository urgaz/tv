from statistic.models import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date, datetime, timedelta
from functions.main import *
from functions.deco import *
from statistic.views.update import ReportEditView



@login_required
def workers_all(request):
    workers = Worker.objects.all()
    context = {'workers': workers}
    return render(request, 'views/workers_all.html', context)

@login_required
def stanoks_all(request):
    query = Stanok.objects.all()
    context = {'stanoks': query}
    return render(request, 'views/stanoks_all.html', context)


# @login_required
# def reports_all(request):
#     query = Report.objects.all()
#     context = {'reports': query}
#     return render(request, 'views/reports_all.html', context)


@login_required
def reports_all(request, st, year, month, day):
    obj = Report.objects.all().order_by('-date', 'stanok__number', 'value')
    
    if year != 0:
        obj = obj.filter(date__year=year)
    if month != 0:
        obj = obj.filter(date__month=month)
    if day != 0:
        obj = obj.filter(date__day=day)
    if st != 'Jami':
        obj = obj.filter(stanok__number=st)
        
    values = []
    for i in obj:
        values.append(int(i.value) + int(i.value2) + int(i.value3))

    context = {'reports': obj, 'year': year, 'month': month, 'day': day, 'st': st, 'values': values}
    context['years'] = ['2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027']
    context['months'] = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    context['days'] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    
    context['stanoks'] = Stanok.objects.all()
    # context['path'] = ps
    
    return render(request, 'views/reports_all.html', context)


@login_required
def smena_all(request):
    smena = Smena.objects.all()
    context = {'smena': smena}
    return render(request, 'views/smena_all.html', context)



@login_required
def surface_all(request, sm, year, month, day):
    obj = Surface.objects.all().order_by('-date', 'smena')
    
    if year != 0:
        obj = obj.filter(date__year=year)
    if month != 0:
        obj = obj.filter(date__month=month)
    if day != 0:
        obj = obj.filter(date__day=day)
    if sm != 'Jami':
        obj = obj.filter(smena__no=str(sm))
        
    values = []
    # for i in obj:
    #     values.append(int(i.value) + int(i.value2) + int(i.value3))

    context = {'surface': obj, 'year': year, 'month': month, 'day': day, 'sm': sm, 'values': values}
    context['years'] = ['2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027']
    context['months'] = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    context['days'] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    
    context['smena'] = Smena.objects.all()
    # context['path'] = ps
    
    return render(request, 'views/surface_all.html', context)
