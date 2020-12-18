import pyodbc

MDB = "C:\\Users\\nio74\\Desktop\\dati.mdb"
DRV = "{Microsoft Access Driver (*.mdb)}"
PWD = "gmpa"

con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV,MDB,PWD))
cur = con.cursor()

for row in cur.tables():
    print (row.tabmag)

    cur.close()
    con.close()
