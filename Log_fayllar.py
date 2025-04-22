# --------------------LOG FAYLLAR -----------------------
import logging

# logging.basicConfig(filename='app.log' , level=logging.INFO) # LOG FAYL ASHADI
# logging.info('Dastur isledi')
# logging .warning("Bul eskertiw")
# logging.error("Bul qatelik")


# logging.basicConfig(filename="Error.log", level=logging.ERROR)
# try:
#    
#     c=10/0
# except Exception as e:
#     logging.error(f"Qatelik turi :{e}")

# logging.basicConfig(
#     filename="myapp.log",
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S'
# )


# LOg darejelri 5 levelge iye
# DEBUG - Dasturshiler ushin harbir qademdi esaplaydi
# INFO - Tiykargi maglumatlar cod istetedi toqtraydi
# WARMING - Eskertiw
# ERROR- Eskertiw
# CRETICAL -  KODTI TOQTATIN QATELIK


# logging.basicConfig(
#     filename='Qatelik.log',
#     level=logging.INFO   

# )
# try:
#     a={"Python"}
#     b=a["y"]
# except Exception as e:
#     logging.error(f"Bul qate: {e}")
 


# logging.basicConfig("Error.log",level=Warning)
# logging.warning("Qate kod")



import logging
logger=logging.getLogger()
logger.setLevel(logging.INFO)

# Faylga jaziw bolim
# file_hamder = logging.FileHandler("test.log")
# file_hamder.setLevel(logging.INFO)

# #Consolga jaziw bolimi
# console_hander = logging.StreamHandler()
# console_hander.setLevel(logging.INFO)





# a = logging.FileHandler("test.log")
# a.setLevel(logging.INFO)
# try:
#     a='15'
#     b=5
#     print(a/b)
# except Exception as e:
#     print(e)

#ham consulga ham faylga log jaziw
import logging



logger = logging.getLogger()
logger.setLevel(logging.INFO)

#Fayilga jaziw bolimi

file_handler = logging.FileHandler("testss.log")
file_handler.setLevel(logging.INFO)

#Consulga jaziw bolimi

consule_handler = logging.StreamHandler()
consule_handler.setLevel(logging.INFO)


#Formatlari
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
consule_handler.setFormatter(formatter)

#Handlerdi biriktiriw

logger.addHandler(file_handler)
logger.addHandler(consule_handler)

#Test logger
logger.info("Bul log fayilga ham konsulga shigiwshi soz")

