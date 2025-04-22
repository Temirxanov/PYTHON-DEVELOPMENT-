# import json
# import logging
# logging.basicConfig(filename='Json_fayldagi_qatelik.log', level=logging.ERROR)

# try:
#     with open("test.json",'r')as file:
#         date = json.load(file)
#         print(date)
# except Exception as x:
#     logging.error("JSON File da qatelik juz berdi {x} ")

# Har kunlik file jaratiw ushin 
# import logging
# from logging.handlers import TimedRotatingFileHandler
# logger = logging.getLogger("Longer_fayl")
# logger.setLevel(logging.INFO)
# ozgeriwshi = TimedRotatingFileHandler('log_file', when='mindnig', interval=1 , backupCount=7)


# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# ozgeriwshi.setFormatter(formatter)
# logger.addHandler(ozgeriwshi)
# logger.info("Bul jerdegi fayllar jan`alandi")


# import logging
# logging.basicConfig("contact.log" , level=logging.INFO)
# format=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# a=input("Paydalaniwshi ati han Nomeri:")
# logging.info(f"Paydalaniwshi kontakti : {a}")


# from logging.handlers import TimedRotatingFileHandler
# import logging
# logger = logging.getLogger("logger_fayl")
# logger.setLevel(logging.INFO)
# parol = ' 12345678'
# soraw = input("Parol jazin : ")


# ozgeriwshi = TimedRotatingFileHandler('logs',when="midnight",interval=1,backupCount=7)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# ozgeriwshi.setFormatter(formatter)

# logger.addHandler(ozgeriwshi)
# a=input(f"Paydalaniwshi ati :")
# b = input("Nomeri :")

# logger.info(f"Ati:{a}\nNomeri:{b}")






# from logging.handlers import TimedRotatingFileHandler
# import logging
# logger = logging.getLogger("logger_fayl")
# logger.setLevel(logging.INFO)
# parol = ' 12345678'
# soraw = input("Parol jazin : ")
# sanaw = 0
# while sanaw==0:
#     sanaw+=1
# if soraw != parol:
    
        
#     ozgeriwshi = TimedRotatingFileHandler('logs',when="midnight",interval=1,backupCount=7)
#     formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#     ozgeriwshi.setFormatter(formatter)

#     logger.addHandler(ozgeriwshi)
#     logger.info(f"{sanaw} ret qate kiritdin Qate parol\nDuris parol:{parol}")
# else:
#     print("parol duris")
    


# list = [1,1,2,2,3,3,4,4,5,6,6,7,7]
# for san in list:
#     qaytalaw=0
#     for i in list:
#         if i==san:



product = [
    {'Ati':'alma','Katigoriya':'miywe','summasi':5000},
    {'Ati':'almurt','Katigoriya':'miywe','summasi':5000},
    {'Ati':'banan','Katigoriya':'miywe','summasi':5000},
    {'Ati':'may','Katigoriya':'onim','summasi':1200},
    {'Ati':'','Katigoriya':'Paliz','summasi':5000},
    {'Ati':'alma','Katigoriya':'miywe','summasi':5000},
    {'Ati':'almurt','Katigoriya':'miywe','summasi':5000},
    {'Ati':'banan','Katigoriya':'miywe','summasi':5000},
    {'Ati':'may','Katigoriya':'onim','summasi':1200},
    {'Ati':'','Katigoriya':'Paliz','summasi':5000},
]

