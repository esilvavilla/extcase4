import pandas as pd
import psycopg2
from sqlalchemy import create_engine, text


POSTGRES_ADDRESS = 'extcase-week4.ccb9ylgqjq1z.us-east-2.rds.amazonaws.com' ## INSERT YOUR DB ADDRESS
POSTGRES_PORT = '5432'
POSTGRES_USERNAME = 'postgres' ## CHANGE THIS TO YOUR POSTGRES USERNAME
POSTGRES_PASSWORD = 'KGhA2EJlA2K7mVB5ynpJ' ## CHANGE THIS TO YOUR POSTGRES PASSWORD 
POSTGRES_DBNAME = 'extcase-week4' ## CHANGE THIS TO YOUR DATABASE NAME

postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'
                .format(username=POSTGRES_USERNAME,
                 password=POSTGRES_PASSWORD,
                 ipaddress=POSTGRES_ADDRESS,
                 port=POSTGRES_PORT,
                 dbname=POSTGRES_DBNAME))
# Create the connection
engine=create_engine(postgres_str)

df = pd.read_sql("SELECT * from trades;", engine.connect(), parse_dates={'Entry-time': {'format': '%d %m %y %H:%M'}})

