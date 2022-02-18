from app.forms import Service_net_useForm
from django.shortcuts import render
from django.http import FileResponse
from app.forms import *
from urgaz_tutorials.settings import BASE_DIR as dir
import os
from functions.main import *
def services(request):
    return render(request, 'views/services/services.html')




def service_get_ip(request):
    # print(request.META)
    ip = get_ip(request)
    context = {'ip': ip}
    return render(request, 'views/services/get_ip.html', context)


def service_net_use(request):
    if request.method == 'POST':
        bbf = Service_net_useForm(request.POST)
        if bbf.is_valid():
            ip = get_ip(request)
            # os.system('fsutil file createnew {} 0'.format(BASE_DIR, 'files\\start.cmd'))
            # except:
            #     null = True
            file_path = os.path.join(dir, 'files\\start{}.cmd'.format(ip))
            f = open(file_path, 'w')
            f.write("start \\\\"+str(bbf.cleaned_data['ip']))

            f.close()
            context = {'path': file_path}
            return render(request, 'views/services/net_use.html', context)
        else:
            return render(request, 'views/services/net_use.html')
    else:
        bbf = Service_net_useForm()
        context = {'form': bbf}
        return render(request, 'views/services/net_use.html', context)

def service_get_net_use(request, file):
    f =open(file, 'rb')
    return FileResponse(f)


def service_install_printers(request):
    return render(request, 'views/services/install_printers.html')

# def service_install_local_printer(request):
    




def service_turnoff_auto_update(request, file):
    
    if file == "True":
        f = open('files/service_turnoff_auto_update.cmd', 'rb')
        return FileResponse(f)
    else:
        return render(request, 'views/services/turnoff_auto_update.html')