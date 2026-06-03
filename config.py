import urllib
from sqlalchemy import create_engine

DRIVER = '{ODBC Driver 17 for SQL Server}' 

SERVER = '.' 

SOURCE_CONN_STR = f"DRIVER={DRIVER};SERVER={SERVER};DATABASE=WideWorldImporters;Trusted_Connection=yes;Encrypt=yes;TrustServerCertificate=yes;"

params = urllib.parse.quote_plus(f"DRIVER={DRIVER};SERVER={SERVER};DATABASE=WideWorldImporters_DW;Trusted_Connection=yes;Encrypt=yes;TrustServerCertificate=yes;")
TARGET_ENGINE = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)