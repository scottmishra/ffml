import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to an existing database 172.17.0.2, postgres, pass
default_db = "postgres"
password = "pass"
user = "postgres"

conn = psycopg2.connect(dbname=default_db, password=password, user=user)
print conn
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
cur.execute("CREATE DATABASE nfldb")
#cur.execute(open("nfldb.sql", "r").read())
print "Finished importing"
cur.close()
conn.close()
