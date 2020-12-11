import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\nio74\Desktop\datiprova.mdb;PWD=gmpa;')
cursor = conn.cursor()