import pywhatkit
from datetime import datetime
import time

second=time.time()+60

date = datetime.fromtimestamp(second)

pywhatkit.sendwhatmsg("+57 3227879774", "prueba bot",date.hour,date.minute)


time.sleep(10)

pywhatkit.sendwhats_image("+573227879774","Photos\cat.jpg" )

