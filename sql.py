from psycopg2.extras import RealDictCursor
import psycopg2
from contextlib import closing

dbname = 'colordb'
dbuser = 'postgres'
dbpassword = '1'
dbhost = 'localhost'


def execute(sql, vars):
    with closing(psycopg2.connect(dbname=dbname, user=dbuser, password=dbpassword, host=dbhost)) as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql, vars)
            conn.commit()


def execute_array(sql_array):
    with closing(psycopg2.connect(dbname=dbname, user=dbuser, password=dbpassword, host=dbhost)) as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            for n in sql_array:
                cur.execute(n[0], n[1])
            conn.commit()


def select(sql, vars):
    with closing(psycopg2.connect(dbname=dbname, user=dbuser, password=dbpassword, host=dbhost)) as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql, vars)
            return cur.fetchall()