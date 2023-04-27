from flask import Flask
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from models import PricingData
import os
from datetime import datetime
from dotenv import load_dotenv
import logging as logger


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
    return 'Base Pricing Route'

# Service to return most recent price for given ticker
@app.route('/price/<base>/<quote>')
def get_price(base, quote):

    # Format expected ticker
    ticker = base + '-' + quote
  
    # Grab most recent row for given ticker (always returns 1 row)
    query = session.query(PricingData).filter(PricingData.ticker == ticker).\
        order_by(PricingData.datetime.desc()).limit(1)
    
    # Always returns 1 row
    for row in query:
        json_return = {
            "datetime": row.datetime.strftime("%m-%d-%Y %H:%M:%S"),
            "ticker": row.ticker,
            "close_price": row.close
        }

    return json_return


if __name__ == '__main__':
    # Force to run on specific ports set in env vars
    app.run(host=os.environ.get('HTTP_HOST'),
        port=int(os.environ.get('HTTP_PORT')))