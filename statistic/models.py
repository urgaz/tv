from django.db import models
from django.db.models.fields import CharField, DateField
from django.db.models.fields.related import ForeignKey, ManyToManyField

class Worker(models.Model):
    name = CharField(null=True, blank=False, max_length=100)
    date_bday = DateField(db_index=True, null=True, blank=False)
    def __str__(self) -> str:
        return self.name
class Stanok(models.Model):
    title = CharField(null=True, max_length=20, blank=True)
    number = CharField(null=True, max_length=5, blank=False)
    workers = ManyToManyField('Worker', blank=True)
    norma_value = CharField(null=True, max_length=20, blank=True)
    def __str__(self) -> str:
        return '{}. {}'.format(self.number, self.title)

class Report(models.Model):
    date = DateField(null=True, blank=False, max_length=20)
    stanok = ForeignKey('Stanok', null=True, blank=False, on_delete=models.PROTECT)
    value = CharField(null=True, max_length=10, blank=False)  # atqi 1-smena
    shift = CharField(null=True, max_length=5, blank=True) #smena    ##### unneccassary
    value2 = CharField(null=True, max_length=10, blank=False)  # atqi2 2-smena
    value3 = CharField(null=True, max_length=10, blank=False)  # atqi3 3-smena

# class Surface(models.Model):
#     date = DateField(null=True, blank=False, max_length=20)
#     smena = ForeignKey('Smena', null=True, blank=False, on_delete=models.PROTECT)
#     soni = models.FloatField(null=True, blank=False)
#     sklad = models.FloatField(null=True, blank=False)  # m2
#     lenta = models.FloatField(null=True, blank=False)   # soati
#     m2 = models.FloatField(null=True, blank=False) # soatiga
#     kley_st_m2 = models.FloatField(null=True, blank=False)
#     kley_st = models.FloatField(null=True, blank=False)  # soatiga

# class Smena(models.Model):
#     no = CharField(null=True, max_length=10, blank=True)
#     master = CharField(null=True, max_length=100, blank=True)
#     norma_lenta = models.FloatField(null=True, blank=False)
#     norma_kley = models.FloatField(null=True, blank=False)
#     organization = CharField(null=True, max_length=20, blank=True, choices=(('urgaz', 'urgaz'), ('kamalak', 'kamalak')))
#     def __str__(self) -> str:
#         return self.no + " " + self.organization