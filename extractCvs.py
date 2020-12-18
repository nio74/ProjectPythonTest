import sys, subprocess, os
from io import StringIO
import pandas as pd
VERBOSE = True

DATABASE = "C:/Users/nio74/Desktop/dati.mdb"
subprocess.run(["C:/Users/nio74/Desktop/ProjectPython/test/mdbtools/mdb-schema",DATABASE,"mysql"])

# Get the list of table names with "mdb-tables"
table_names = subprocess.Popen(["mdb-tables", "-1", DATABASE],
                                   stdout=subprocess.PIPE).communicate()[0]
tables = table_names.splitlines()
sys.stdout.flush()
# Dump each table as a stringio using "mdb-export",
out_tables = {}
for rtable in tables:
    table = rtable.decode()
    if VERBOSE: print('running table:',table)
    if table != '':
        if VERBOSE: print("Dumping " + table)
        contents = subprocess.Popen(["mdb-export", DATABASE, table],
                                    stdout=subprocess.PIPE).communicate()[0]
        temp_io = StringIO(contents.decode())
        print(table, temp_io)
        out_tables[table] = pd.read_csv(temp_io)