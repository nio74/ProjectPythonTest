import pyodbc

conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\nio74\Desktop\dati.mdb;PWD=gmpa;')
#conn = pyodbc.connect('DSN=Dati2;')

cursor = conn.cursor()