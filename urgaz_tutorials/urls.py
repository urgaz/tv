"""urgaz_tutorials URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path

    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""






from django.conf import settings
from django.conf.urls.static import static
from os import name
from django.contrib import admin
from django.urls import path
from app.views.main import *
from app.views.service import *
from app.views.instructions import *

############################
from statistic.views.main import *
from statistic.views.list import *
from statistic.views.statistic import urgaz, kamalak
from statistic.views.create import *
from statistic.views.update import *
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView

urlpatterns = [
    ##########   APP
    path('xiidot1303/', admin.site.urls),
    path('', main, name='main'),
    # services
    path('services', services, name='services'),
    path('service/get_ip', service_get_ip, name='service_get_ip'),
    path('service/net_use', service_net_use, name='service_net_use'),
    path('service/get/net_use/<str:file>/', service_get_net_use, name='service_get_net_use'),
    path('service/install_printers', service_install_printers, name='service_install_printers'),
    path('service/service_turnoff_auto_update/<str:file>/', service_turnoff_auto_update, name='service_turnoff_auto_update'),
    
    # instructions
    path('instructions', instructions, name='instructions'),
    path('instructions/group_outlook', group_outlook, name='group_outlook'),



    # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    ######## STATISTIC
    path('statistic/<int:smena>/', statistic_menu, name='statistic'),
    path('statistic/table', statistic_table, name='statistic_table'),
    path('statistic/table/daily', statistic_table_dayly, name='statistic_table_dayly'),
    path('accounts/login/', LoginView.as_view()),
    path('statistic', main_menu, name='main_menu'),
    path('statistic/three', three, name='statistic_three'),

    #kleyka
    # path('statistic/kleyka/<str:organization>/', kleyka, name='statistic_kleyka'),

    # ######## STATISTIC KAMALAK
    # path('statistic/kamalak/<int:smena>/', kamalak.statistic_menu, name='statistic_kamalak'),
    # path('statistic/kamalak/table', kamalak.statistic_table, name='statistic_kamalak_table'),
    # path('statistic/kamalak/table/daily', kamalak.statistic_table_dayly, name='statistic_kamalak_table_dayly'),


    #workers
    path('workers/all', workers_all, name='workers_all'),
    path('create/worker', WorkerCreateView.as_view(), name='create_worker'),

    #stanok
    path('tools/all', stanoks_all, name='stanok_all'),
    path('create/tool', StanokCreateView.as_view(), name='create_stanok'),
    path('update/tool/<int:pk>', StanokEditView.as_view(), name='update_stanok'),

    #report
    path('reports/all/<str:st>/<int:year>/<int:month>/<int:day>/', reports_all, name='reports_all'),
    path('create/report', ReportCreateView.as_view(), name='create_report'),
    path('update/report/<int:pk>/<str:st>/<int:year>/<int:month>/<int:day>/', ReportEditView.as_view(), name='update_report'),

    # #smena
    # path('create/smena', SmenaCreateView.as_view(), name='create_smena'),
    # path('smena/all', smena_all, name='smena_all'),
    # path('update/smena/<int:pk>/', SmenaEditView.as_view(), name='update_smena'),

    # #surface
    # path('create/surface', SurfaceCreateView.as_view(), name='create_surface'),
    # path('surface/all/<str:sm>/<int:year>/<int:month>/<int:day>/', surface_all, name='surface_all'),
    # path('update/surface/<int:pk>/<str:sm>/<int:year>/<int:month>/<int:day>/', SurfaceEditView.as_view(), name='update_surface'),

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
