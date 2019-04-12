# https://towardsdatascience.com/feature-engineering-in-sql-and-python-a-hybrid-approach-b52347cd2de4
# converted MySQL to Postgres

import os
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# conn = psycopg2.connect(
#     host=localhost,
#     port=5432,
#     dbname='ecommerce',
#     user='postgres',
# )
# cur = conn.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, num integer, data varchar);")
# cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abcdef"))
# cur.execute("SELECT * FROM test;")
# result = cur.fetchone()
# print(result)
# conn.commit()
# cur.close()

engine = create_engine('postgresql://postgres:postgres@localhost:5432/ecommerce') # postgresql://user:password@host_ip:port/database

path = os.path.dirname(os.path.realpath(__file__))

online_filename = os.path.join(path, 'online.csv')
df_online = pd.read_csv(online_filename)
df_online.to_sql('online', engine, if_exists='replace')

order_filename = os.path.join(path, 'order.csv')
df_online = pd.read_csv(order_filename)
df_online.to_sql('purchase', engine, if_exists='replace')

data = pd.read_sql('SELECT * FROM purchase', engine)
print(data)

sql = 'SELECT index, event2 FROM online'
df = pd.read_sql_query(sql, engine).set_index('index')

df = df.sample(frac=1)

train_frac = 0.9
test_frac = 1 - train_frac

trn_cutoff = int(len(df)*train_frac)

df_trn = df[:trn_cutoff]
df_tst = df[trn_cutoff:]

df_trn.to_sql('trn_set', engine, if_exists='replace')
df_tst.to_sql('tst_set', engine, if_exists='replace')


def load_dataset(split="trn_set", limit=None, ignore_categorical=False):
    sql = """
        SELECT 
            o.*
            ,f1.*
            ,f2.*
            ,f3.*
            ,f4.*
            ,EXTRACT( MONTH FROM o.dt::date) AS month
        FROM %s AS t 
        JOIN Online AS o ON t.index = o.index 
        JOIN features_group_1 AS f1 ON t.index = f1.index
        JOIN features_group_2 AS f2 ON t.index = f2.index
        JOIN features_group_3 AS f3 ON t.index = f3.index
        JOIN features_group_4 AS f4 ON t.index = f4.index
        """ % split
    if limit:
        sql += " LIMIT %i"%limit
    print(sql)    
    df = pd.read_sql_query(sql.replace('\n', " ").replace("\t", " "), engine)
    df.event1 = df.event1.fillna(0)
    X = df.drop(["index", "event2", "dt", "day", "session", "visitor", "custno"], axis=1)
    Y = df.event2
    return X, Y

X_trn, Y_trn = load_dataset("trn_set", limit=5)
print(X_trn.head().T)