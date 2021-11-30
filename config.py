from dotenv import load_dotenv
import os

load_dotenv()
user = os.environ.get('MYSQL_USER')
password = os.environ.get('MYSQL_PASSWORD')
host = os.environ.get('MYSQL_HOST')
database = os.environ.get('MYSQL_DATABASE')

url = f'mysql://{user}:{password}@{host}/{database}'
