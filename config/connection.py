import pandas as pd
from sqlalchemy import create_engine
import config.variables as var



def call_mysql(db, table, q):
    try:
        engine = create_engine(f"mysql+pymysql://{var.user}:{var.password}@127.0.0.1/{db}")
        if q == '*':
            query = f"SELECT * FROM {table};"
        else:
            query = q
        data_raw = pd.read_sql(query, engine)
        data = pd.DataFrame(data_raw)
        return data
    except Exception as e:
        print(f"Error collecting data: {e}")


def upload_sql(db, table, data):
    engine = create_engine(f"mysql+pymysql://{var.user}:{var.password}@127.0.0.1/{db}")
    data.to_sql(name = table, con = engine, if_exists="replace", index=False)
