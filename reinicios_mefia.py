#enconding: utf-8
from selenium import webdriver
#import win32com.client as win32
#from docx import Document
#from docx.shared import Cm
#from datetime import datetime
#import win32api, sys, os
import pyautogui
import time

#usuario ='Gestionasic'
#password='T3g5m6x2r9f4v7g8'
pyautogui.moveTo(328, 1066)
time.sleep(3)
pyautogui.click(467,982)
time.sleep(3)
pyautogui.moveTo(165, 1060)
time.sleep(3)
pyautogui.click(165, 1060)
time.sleep(2)
pyautogui.click(318,976)
time.sleep(2)


#--------ingreso al 172.16.231.99:7006-----------


#Logueo de usuario
pyautogui.moveTo(1686, 391)
time.sleep(2)
pyautogui.click(1686, 391)
time.sleep(2)
pyautogui.moveTo(1731, 438)
time.sleep(2)
pyautogui.click(1731, 438)
time.sleep(2)
pyautogui.moveTo(1820, 440)
time.sleep(2)
pyautogui.click(1820, 440)
time.sleep(2)
#ir al servicio Omnia
pyautogui.moveTo(17, 298)
time.sleep(2)
pyautogui.click(17, 298)
time.sleep(2)
pyautogui.moveTo(72, 314)
time.sleep(2)
pyautogui.click(72, 314)
time.sleep(2)
pyautogui.moveTo(387, 192)
time.sleep(2)
pyautogui.click(387, 192)

#primer pantallazo al 172.16.231.99:7006
time.sleep(4)

#Captura de pantalla
captura = pyautogui.screenshot()
toma='1er screen 99_7006'
captura.save(str (toma)+".jpg")
'''toma = time.time( )
captura.save(str (toma)+".jpg")'''

#bajar Omnia server del 172.16.231.99:7006
time.sleep(2)
pyautogui.moveTo(300, 478)
time.sleep(2)
pyautogui.click(300, 478)

time.sleep(2)
pyautogui.moveTo(522, 502)
time.sleep(2)
pyautogui.click(522, 502)

time.sleep(2)
pyautogui.moveTo(555, 549)
time.sleep(2)
pyautogui.click(555, 549)
#Matar servicio
time.sleep(2)
pyautogui.moveTo(288, 303)
time.sleep(2)
pyautogui.click(288, 303)

#---------ingreso al 172.16.231.129:7006-----------
time.sleep(2)
pyautogui.moveTo(347, 11)
time.sleep(2)
pyautogui.click(347, 11)
time.sleep(2)

#Logueo de usuario
pyautogui.moveTo(1686, 391)
time.sleep(2)
pyautogui.click(1686, 391)
time.sleep(2)
pyautogui.moveTo(1731, 438)
time.sleep(2)
pyautogui.click(1731, 438)
time.sleep(2)
pyautogui.moveTo(1820, 440)
time.sleep(2)
pyautogui.click(1820, 440)

#ir al servicio Omnia
pyautogui.moveTo(17, 298)
time.sleep(2)
pyautogui.click(17, 298)
time.sleep(2)
pyautogui.moveTo(72, 314)
time.sleep(2)
pyautogui.click(72, 314)
time.sleep(2)
pyautogui.moveTo(387, 192)
time.sleep(2)
pyautogui.click(387, 192)

#primer pantallazo al 172.16.231.129:7006
time.sleep(4)

#Captura de pantalla
captura = pyautogui.screenshot()
toma='1er screen 129_7006'
captura.save(str (toma)+".jpg")

#bajar Omnia server del 172.16.231.129:7006
time.sleep(2)
pyautogui.moveTo(300, 478)
time.sleep(2)
pyautogui.click(300, 478)

time.sleep(2)
pyautogui.moveTo(522, 502)
time.sleep(2)
pyautogui.click(522, 502)

time.sleep(2)
pyautogui.moveTo(555, 549)
time.sleep(2)
pyautogui.click(555, 549)

#Matar servicio
time.sleep(2)
pyautogui.moveTo(288, 303)
time.sleep(2)
pyautogui.click(288, 303)

#---------ingreso al 172.16.231.130:7006-----------
time.sleep(2)
pyautogui.moveTo(579, 22)
time.sleep(2)
pyautogui.click(579, 22)
time.sleep(2)

#Logueo de usuario
pyautogui.moveTo(1686, 391)
time.sleep(2)
pyautogui.click(1686, 391)
time.sleep(2)
pyautogui.moveTo(1731, 438)
time.sleep(2)
pyautogui.click(1731, 438)
time.sleep(2)
pyautogui.moveTo(1820, 440)
time.sleep(2)
pyautogui.click(1820, 440)

#ir al servicio Omnia
pyautogui.moveTo(17, 298)
time.sleep(2)
pyautogui.click(17, 298)
time.sleep(2)
pyautogui.moveTo(72, 314)
time.sleep(2)
pyautogui.click(72, 314)
time.sleep(2)
pyautogui.moveTo(387, 192)
time.sleep(2)
pyautogui.click(387, 192)

#primer pantallazo al 172.16.231.130:7006
time.sleep(4)

#Captura de pantalla
captura = pyautogui.screenshot()
toma='1er screen 130_7006'
captura.save(str (toma)+".jpg")

#bajar Omnia server del 172.16.231.130:7006
time.sleep(2)
pyautogui.moveTo(300, 478)
time.sleep(2)
pyautogui.click(300, 478)

time.sleep(2)
pyautogui.moveTo(522, 502)
time.sleep(2)
pyautogui.click(522, 502)

time.sleep(2)
pyautogui.moveTo(555, 549)
time.sleep(2)
pyautogui.click(555, 549)

#Matar servicio
time.sleep(2)
pyautogui.moveTo(288, 303)
time.sleep(2)
pyautogui.click(288, 303)

#---------ingreso al 172.16.231.198:7006-----------
time.sleep(2)
pyautogui.moveTo(857, 12)
time.sleep(2)
pyautogui.click(857, 12)
time.sleep(2)

#Logueo de usuario
pyautogui.moveTo(1686, 391)
time.sleep(2)
pyautogui.click(1686, 391)
time.sleep(2)
pyautogui.moveTo(1731, 438)
time.sleep(2)
pyautogui.click(1731, 438)
time.sleep(2)
pyautogui.moveTo(1820, 440)
time.sleep(2)
pyautogui.click(1820, 440)

#ir al servicio Omnia
pyautogui.moveTo(17, 298)
time.sleep(2)
pyautogui.click(17, 298)
time.sleep(2)
pyautogui.moveTo(72, 314)
time.sleep(2)
pyautogui.click(72, 314)
time.sleep(2)
pyautogui.moveTo(387, 192)
time.sleep(2)
pyautogui.click(387, 192)

#primer pantallazo al 172.16.231.198:7006
time.sleep(4)

#Captura de pantalla
captura = pyautogui.screenshot()
toma='1er screen 198_7006'
captura.save(str (toma)+".jpg")

#bajar Omnia server del 172.16.231.198:7006
time.sleep(2)
pyautogui.moveTo(300, 478)
time.sleep(2)
pyautogui.click(300, 478)

time.sleep(2)
pyautogui.moveTo(522, 502)
time.sleep(2)
pyautogui.click(522, 502)

time.sleep(2)
pyautogui.moveTo(555, 549)
time.sleep(2)
pyautogui.click(555, 549)

#Matar servicio
time.sleep(2)
pyautogui.moveTo(288, 303)
time.sleep(2)
pyautogui.click(288, 303)

#---------ingreso al 172.16.231.199:7006-----------
time.sleep(2)
pyautogui.moveTo(1106, 13)
time.sleep(2)
pyautogui.click(1106, 13)
time.sleep(2)

#Logueo de usuario
pyautogui.moveTo(1686, 391)
time.sleep(2)
pyautogui.click(1686, 391)
time.sleep(2)
pyautogui.moveTo(1731, 438)
time.sleep(2)
pyautogui.click(1731, 438)
time.sleep(2)
pyautogui.moveTo(1820, 440)
time.sleep(2)
pyautogui.click(1820, 440)

#ir al servicio Omnia
pyautogui.moveTo(17, 298)
time.sleep(2)
pyautogui.click(17, 298)
time.sleep(2)
pyautogui.moveTo(72, 314)
time.sleep(2)
pyautogui.click(72, 314)
time.sleep(2)
pyautogui.moveTo(387, 192)
time.sleep(2)
pyautogui.click(387, 192)

#primer pantallazo al 172.16.231.199:7006
time.sleep(4)

#Captura de pantalla
captura = pyautogui.screenshot()
toma='1er screen 199_7006'
captura.save(str (toma)+".jpg")

#bajar Omnia server del 172.16.231.199:7006
time.sleep(2)
pyautogui.moveTo(300, 478)
time.sleep(2)
pyautogui.click(300, 478)

time.sleep(2)
pyautogui.moveTo(522, 502)
time.sleep(2)
pyautogui.click(522, 502)

time.sleep(2)
pyautogui.moveTo(555, 549)
time.sleep(2)
pyautogui.click(555, 549)

#Matar servicio
time.sleep(2)
pyautogui.moveTo(288, 303)
time.sleep(2)
pyautogui.click(288, 303)

#pyautogui.typewrite("Gestionasic")

'''
#--------ingreso al 172.16.231.99:7008-----------
time.sleep(200)
pyautogui.moveTo(165, 1060)
time.sleep(3)
pyautogui.click(165, 1060)
time.sleep(2)
pyautogui.moveTo(547, 971)
time.sleep(2)
pyautogui.click(547, 971)
time.sleep(2)

#Logueo de usuario
pyautogui.moveTo(1686, 391)
time.sleep(2)
pyautogui.click(1686, 391)
time.sleep(2)
pyautogui.moveTo(1731, 438)
time.sleep(2)
pyautogui.click(1731, 438)
time.sleep(2)
pyautogui.moveTo(1820, 440)
time.sleep(2)
pyautogui.click(1820, 440)
time.sleep(2)
#ir al servicio Mefia server y srvProxy1
pyautogui.moveTo(17, 298)
time.sleep(2)
pyautogui.click(17, 298)
time.sleep(2)
pyautogui.moveTo(72, 314)
time.sleep(2)
pyautogui.click(72, 314)
time.sleep(2)
pyautogui.moveTo(387, 192)
time.sleep(2)
pyautogui.click(387, 192)

#primer pantallazo al 172.16.231.99:7008
time.sleep(4)

#Captura de pantalla
captura = pyautogui.screenshot()
toma='1er screen 99_7008'
captura.save(str (toma)+".jpg")


#bajar Mefia server y srvProxy1 del 172.16.231.99:7008
time.sleep(2)
pyautogui.moveTo(300, 450)
time.sleep(2)
pyautogui.click(300, 450)
time.sleep(2)
pyautogui.moveTo(300, 478)
time.sleep(2)
pyautogui.click(300, 478)

time.sleep(2)
pyautogui.moveTo(522, 502)
time.sleep(2)
pyautogui.click(522, 502)

time.sleep(2)
pyautogui.moveTo(555, 549)
time.sleep(2)
pyautogui.click(555, 549)
#Matar servicio

time.sleep(2)
pyautogui.moveTo(288, 303)
time.sleep(2)
pyautogui.click(288, 303)

#---------ingreso al 172.16.231.129:7008-----------
time.sleep(2)
pyautogui.moveTo(347, 11)
time.sleep(2)
pyautogui.click(347, 11)
time.sleep(2)

#Logueo de usuario
pyautogui.moveTo(1686, 391)
time.sleep(2)
pyautogui.click(1686, 391)
time.sleep(2)
pyautogui.moveTo(1731, 438)
time.sleep(2)
pyautogui.click(1731, 438)
time.sleep(2)
pyautogui.moveTo(1820, 440)
time.sleep(2)
pyautogui.click(1820, 440)

#ir al servicio Mefia server y srvProxy1
pyautogui.moveTo(17, 298)
time.sleep(2)
pyautogui.click(17, 298)
time.sleep(2)
pyautogui.moveTo(72, 314)
time.sleep(2)
pyautogui.click(72, 314)
time.sleep(2)
pyautogui.moveTo(387, 192)
time.sleep(2)
pyautogui.click(387, 192)

#primer pantallazo al 172.16.231.129:7008
time.sleep(4)

#Captura de pantalla
captura = pyautogui.screenshot()
toma='1er screen 129_7008'
captura.save(str (toma)+".jpg")

#bajar Mefia server y srvProxy1 del 172.16.231.129:7008
time.sleep(2)
pyautogui.moveTo(300, 450)
time.sleep(2)
pyautogui.click(300, 450)
time.sleep(2)
pyautogui.moveTo(300, 478)
time.sleep(2)
pyautogui.click(300, 478)

time.sleep(2)
pyautogui.moveTo(522, 502)
time.sleep(2)
pyautogui.click(522, 502)

time.sleep(2)
pyautogui.moveTo(555, 549)
time.sleep(2)
pyautogui.click(555, 549)

#Matar servicio
time.sleep(2)
pyautogui.moveTo(288, 303)
time.sleep(2)
pyautogui.click(288, 303)

#---------ingreso al 172.16.231.130:7008-----------
time.sleep(2)
pyautogui.moveTo(579, 22)
time.sleep(2)
pyautogui.click(579, 22)
time.sleep(2)

#Logueo de usuario
pyautogui.moveTo(1686, 391)
time.sleep(2)
pyautogui.click(1686, 391)
time.sleep(2)
pyautogui.moveTo(1731, 438)
time.sleep(2)
pyautogui.click(1731, 438)
time.sleep(2)
pyautogui.moveTo(1820, 440)
time.sleep(2)
pyautogui.click(1820, 440)

#ir al servicio Mefia server y srvProxy1
pyautogui.moveTo(17, 298)
time.sleep(2)
pyautogui.click(17, 298)
time.sleep(2)
pyautogui.moveTo(72, 314)
time.sleep(2)
pyautogui.click(72, 314)
time.sleep(2)
pyautogui.moveTo(387, 192)
time.sleep(2)
pyautogui.click(387, 192)

#primer pantallazo al 172.16.231.130:7008
time.sleep(4)

#Captura de pantalla
captura = pyautogui.screenshot()
toma='1er screen 130_7008'
captura.save(str (toma)+".jpg")

#bajar Mefia server y srvProxy1 del 172.16.231.130:7008
time.sleep(2)
pyautogui.moveTo(300, 450)
time.sleep(2)
pyautogui.click(300, 450)
time.sleep(2)
pyautogui.moveTo(300, 478)
time.sleep(2)
pyautogui.click(300, 478)

time.sleep(2)
pyautogui.moveTo(522, 502)
time.sleep(2)
pyautogui.click(522, 502)

time.sleep(2)
pyautogui.moveTo(555, 549)
time.sleep(2)
pyautogui.click(555, 549)

#Matar servicio
time.sleep(2)
pyautogui.moveTo(288, 303)
time.sleep(2)
pyautogui.click(288, 303)

#---------ingreso al 172.16.231.198:7008-----------
time.sleep(2)
pyautogui.moveTo(857, 12)
time.sleep(2)
pyautogui.click(857, 12)
time.sleep(2)

#Logueo de usuario
pyautogui.moveTo(1686, 391)
time.sleep(2)
pyautogui.click(1686, 391)
time.sleep(2)
pyautogui.moveTo(1731, 438)
time.sleep(2)
pyautogui.click(1731, 438)
time.sleep(2)
pyautogui.moveTo(1820, 440)
time.sleep(2)
pyautogui.click(1820, 440)

#ir al servicio Mefia server y srvProxy1
pyautogui.moveTo(17, 298)
time.sleep(2)
pyautogui.click(17, 298)
time.sleep(2)
pyautogui.moveTo(72, 314)
time.sleep(2)
pyautogui.click(72, 314)
time.sleep(2)
pyautogui.moveTo(387, 192)
time.sleep(2)
pyautogui.click(387, 192)

#primer pantallazo al 172.16.231.198:7008
time.sleep(4)

#Captura de pantalla
captura = pyautogui.screenshot()
toma='1er screen 198_7008'
captura.save(str (toma)+".jpg")

#bajar Mefia server y srvProxy1 del 172.16.231.198:7008
time.sleep(2)
pyautogui.moveTo(300, 450)
time.sleep(2)
pyautogui.click(300, 450)
time.sleep(2)
pyautogui.moveTo(300, 478)
time.sleep(2)
pyautogui.click(300, 478)

time.sleep(2)
pyautogui.moveTo(522, 502)
time.sleep(2)
pyautogui.click(522, 502)

time.sleep(2)
pyautogui.moveTo(555, 549)
time.sleep(2)
pyautogui.click(555, 549)

#Matar servicio
time.sleep(2)
pyautogui.moveTo(288, 303)
time.sleep(2)
pyautogui.click(288, 303)

#---------ingreso al 172.16.231.199:7008-----------
time.sleep(2)
pyautogui.moveTo(1106, 13)
time.sleep(2)
pyautogui.click(1106, 13)
time.sleep(2)

#Logueo de usuario
pyautogui.moveTo(1686, 391)
time.sleep(2)
pyautogui.click(1686, 391)
time.sleep(2)
pyautogui.moveTo(1731, 438)
time.sleep(2)
pyautogui.click(1731, 438)
time.sleep(2)
pyautogui.moveTo(1820, 440)
time.sleep(2)
pyautogui.click(1820, 440)

#ir al servicio Mefia server y srvProxy1
pyautogui.moveTo(17, 298)
time.sleep(2)
pyautogui.click(17, 298)
time.sleep(2)
pyautogui.moveTo(72, 314)
time.sleep(2)
pyautogui.click(72, 314)
time.sleep(2)
pyautogui.moveTo(387, 192)
time.sleep(2)
pyautogui.click(387, 192)

#primer pantallazo al 172.16.231.199:7008
time.sleep(4)

#Captura de pantalla
captura = pyautogui.screenshot()
toma='1er screen 199_7008'
captura.save(str (toma)+".jpg")

#bajar Mefia server y srvProxy1 del 172.16.231.199:7008
time.sleep(2)
pyautogui.moveTo(300, 450)
time.sleep(2)
pyautogui.click(300, 450)
time.sleep(2)
pyautogui.moveTo(300, 478)
time.sleep(2)
pyautogui.click(300, 478)

time.sleep(2)
pyautogui.moveTo(522, 502)
time.sleep(2)
pyautogui.click(522, 502)

time.sleep(2)
pyautogui.moveTo(555, 549)
time.sleep(2)
pyautogui.click(555, 549)

#Matar servicio
time.sleep(2)
pyautogui.moveTo(288, 303)
time.sleep(2)
pyautogui.click(288, 303)'''
