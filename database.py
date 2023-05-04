from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
load_dotenv()

db_connection_string = os.environ['SECRETSTRING']

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl":{
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

def load_jobs():
    with engine.connect() as conn:
        result = conn.execute(text("select * from Persons"))

    result_dicts = []
    for row in result.all():
        result_dicts.append(row)
    return result_dicts