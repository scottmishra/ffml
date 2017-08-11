import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to an existing database 172.17.0.2, postgres, pass
default_db = "nfldb"
password = "pass"
user = "postgres"

conn = psycopg2.connect(dbname=default_db, password=password, user=user)
print conn
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
cur.execute("insert into team values ('JAX','Jacksonville','Jaguars')")
cur.execute("UPDATE play SET pos_team = 'JAC' WHERE pos_team = 'JAX'")
cur.execute("DELETE FROM team WHERE team_id = 'JAX'")

cur.close()
conn.close()
