from os import remove
from statistic.models import Report, Stanok, Worker
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date, datetime, timedelta
from functions.main import *
from functions.deco import *
from statistic.views.update import ReportEditView




def custom_sort(t):
    return t[1]


@print_ip
def statistic_menu(request, smena):
    current_time = date.today() - timedelta(days=1)
    values_list = []
    for s in Stanok.objects.filter(organization='Urgaz'):
        summary = 0
        for r in Report.objects.filter(stanok__number=s.number, date__month=current_time.month, date__year=current_time.year):
            # def value_to_per(value):
            #     per = round(((float(value)/float(s.norma_value))*100), 2)
                # return per
            if smena == 1:
                summary += int(r.value)
            elif smena == 2:
                summary += int(r.value2)
            elif smena == 3:
                summary += int(r.value3)
        summary_percent = round(((float(summary)/(float(s.norma_value)*current_time.day))*100), 2)

        values_list.append([' St {}'.format(str(s.number)), summary_percent])
    
    values_list.sort(key=custom_sort, reverse=True)
    hundred_percent = values_list[0][1]
    
    result = []
    for i in values_list:
        height = round((((i[1] / hundred_percent) * 100) / 2.5), 1)
        i.append(height)
        i.append(50-height)
    months = ['Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'Iyun', 'Iyul', 'Avgust', 'Sentabr', 'Oktabr', 'Noyabr', 'Dekabr']

    if smena == 3:
        next_page_smena = 1
    else:
        next_page_smena = smena + 1
    context = {'values': values_list, 'current_month': months[current_time.month-1], 'next_page_smena': next_page_smena, 'smena': smena}
    
    return render(request, 'views/statistic_urgaz.html', context)



def custom_sort2(t):
    return t[6]

@print_ip
def statistic_table(request):
    current_time = date.today() - timedelta(days=1)
    values_list = []
    for s in Stanok.objects.filter(organization='Urgaz'):
        summary1 = 0
        summary2 = 0
        summary3 = 0
        for r in Report.objects.filter(stanok__number=s.number, date__month=current_time.month, date__year=current_time.year):
            # def value_to_per(value):
            #     per = round(((float(value)/float(s.norma_value))*100), 2)
                # return per
            
            summary1 += int(r.value)    
            summary2 += int(r.value2)
            summary3 += int(r.value3)
        summary = summary1 + summary2 + summary3
        summary_percent = round(((float(summary)/(float(s.norma_value)*current_time.day))*100), 2)
        norma_atqi = int(s.norma_value)*current_time.day
        stanok_title = '{}. {}'.format(str(s.number), s.title)
        values_list.append([stanok_title, norma_atqi, summary1, summary2, summary3, summary ,summary_percent])
    months = ['Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'Iyun', 'Iyul', 'Avgust', 'Sentabr', 'Oktabr', 'Noyabr', 'Dekabr']
    values_list.sort(key=custom_sort2, reverse=True)
    context = {'values': values_list, 'current_month': months[current_time.month-1]}
    return render(request, 'views/statistic_urgaz_table.html', context)




@print_ip
def statistic_table_dayly(request):
    today = date.today()
    yesterday = today - timedelta(days=1)
    values_list = []

    for r in Report.objects.filter(date__day=yesterday.day, date__month=yesterday.month, date__year=yesterday.year):
        summary = int(r.value) + int(r.value2) + int(r.value3)
        summary_percent = round(((float(summary)/(float(r.stanok.norma_value)))*100), 2)
        stanok_title = '{}. {}'.format(str(r.stanok.number), r.stanok.title)
        values_list.append([stanok_title, r.stanok.norma_value, int(r.value), int(r.value2), int(r.value3), summary, summary_percent])
    values_list.sort(key=custom_sort2, reverse=True)
    
    context = {'values': values_list, 'date': yesterday}
    return render(request, 'views/statistic_urgaz_table_dayly.html', context)




def custom_sort2(t):
    return t[6]


def sort_sovrin(t):
    return t[1]

def three(request):
    today = date.today()
    today = today.replace(day=1)
    current_time = today - timedelta(days=1)
    values_list = []
    for s in Stanok.objects.filter(organization='Urgaz'):
        summary1 = 0
        summary2 = 0
        summary3 = 0
        for r in Report.objects.filter(stanok__number=s.number, date__month=current_time.month, date__year=current_time.year):
            # def value_to_per(value):
            #     per = round(((float(value)/float(s.norma_value))*100), 2)
                # return per
            
            summary1 += int(r.value)    
            summary2 += int(r.value2)
            summary3 += int(r.value3)
        summary = summary1 + summary2 + summary3
        summary_percent = round(((float(summary)/(float(s.norma_value)*current_time.day))*100), 2)
        norma_atqi = int(s.norma_value)*current_time.day
        stanok_title = '{}'.format(str(s.number))
        values_list.append([stanok_title, norma_atqi, summary1, summary2, summary3, summary ,summary_percent])
    months = ['Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'Iyun', 'Iyul', 'Avgust', 'Sentabr', 'Oktabr', 'Noyabr', 'Dekabr']
    values_list.sort(key=custom_sort2, reverse=True)
 
    values_list = values_list[:3]
    
    winner = values_list[0]
    
    sovrin = [['1', winner[2]], ['2', winner[3]], ['3', winner[4]]]
    sovrin.sort(key=sort_sovrin, reverse=True)
    
    for s in sovrin:
        s.append(int((s[1])/winner[1]*100))

    
    context = {'winner': winner[0], 'sovrin': sovrin, 'values': values_list, 'current_month': months[current_time.month-1]}
    return render(request, 'views/three_urgaz.html', context)
