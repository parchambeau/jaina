from flask import Flask
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from models import PricingData
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

# Load env vars
load_dotenv()

# Grab secrets from environment variables
DATABASE_URL = os.environ.get('DATABASE_URL')

# Setup DB connection
engine = create_engine(DATABASE_URL)

# Setup db session
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def base_route():
    return 'Base Route'

# Service to return all USD price of given ticker greater than or equal to timestamp given
@app.route('/price/<ticker>/<int:timestamp>')
def get_price(ticker, timestamp):

    # TODO For testing 1681966800 = 2023-04-20 01:00:00

    data = []

    # Convert timestamp to datetime string to match db
    datetime_string = datetime.fromtimestamp(timestamp)
  
    # Grab all rows with given ticker and past or equal to the timestamp passed in
    query = session.query(PricingData).filter(PricingData.ticker == ticker).\
        filter(PricingData.datetime >= datetime_string)

    for row in query:

        json_return = {
            "datetime": row.datetime.strftime("%m-%d-%Y %H:%M:%S"),
            "ticker": row.ticker,
            "close_price": row.close
        }

        data.append(json_return)

    return data


if __name__ == '__main__':
    # Force to run on specific ports set in env vars
    app.run(host=os.environ.get('HTTP_HOST'),
        port=int(os.environ.get('HTTP_PORT')))