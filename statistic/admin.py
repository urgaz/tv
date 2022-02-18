from django.contrib import admin
from statistic.models import *

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_bday')


class StanokAdmin(admin.ModelAdmin):
    list_display = ('title', 'number')


class ReportAdmin(admin.ModelAdmin):
    list_display = ('date', 'stanok', 'value', 'value2', 'value3')


admin.site.register(Worker, WorkerAdmin)
admin.site.register(Stanok, StanokAdmin)
admin.site.register(Report, ReportAdmin)
