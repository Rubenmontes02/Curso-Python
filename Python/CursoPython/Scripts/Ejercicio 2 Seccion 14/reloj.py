import datetime 
import time 
import os 

while True:
	os.system('cls') # Limpiamos la pantalla

	dt = datetime.datetime.now() # creamos fecha y hora

	print('{}:{}:{}'. format(dt.hour, dt.minute, dt.second))  # Mostramos fecha

	time.sleep(1)  # esperamos 1 segundo 
