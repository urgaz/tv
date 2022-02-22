from django.contrib import admin
from statistic.models import *

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_bday')


class StanokAdmin(admin.ModelAdmin):
    list_display = ('title', 'number')


class ReportAdmin(admin.ModelAdmin):
    list_display = ('date', 'stanok', 'value', 'value2', 'value3')


class SurfaceAdmin(admin.ModelAdmin):
    list_display = ('date', 'smena')

class SmenaAdmin(admin.ModelAdmin):
    list_display = ('no', 'organization', 'master', 'norma_lenta', 'norma_kley')

admin.site.register(Worker, WorkerAdmin)
admin.site.register(Stanok, StanokAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Surface, SurfaceAdmin)
admin.site.register(Smena, SmenaAdmin)