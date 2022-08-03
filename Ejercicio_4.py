import os
from win10toast import ToastNotifier

from datetime import datetime
dt = datetime.now()


## establecer una hora y minuto del día 
print("""Programa para establecer una hora y minuto de un día para un recordatorio
Por favor, Ingrese el día, hora y minuto del evento
Recuerde que se repetirá todos los meses""")

año = (datetime.now().year)
mes = (datetime.now().month)
dia = int(input('Ingrese el día: '))
hora = int(input('Ingrese la hora: '))
min = int(input('Ingrese el minuto: '))
seg = int(00)
microseg = int (000000)

fecha = dt.replace(year = año, month = mes, day = dia, hour = hora, minute = min -5 , second = seg, microsecond = microseg)
y = print(fecha)


## establecer notificación

def notificacion():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    toast = ToastNotifier()
    titulo = "RECORDATORIO"
    mensaje = "Faltan 5 minutos para tu evento"
    time = 5
    icon = None

    toast.show_toast(titulo, mensaje, icon_path=icon, duration=time, threaded=True)
    
    print('Se está mostrando una notificación en windows')
notificacion()

