from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Numeric

Base = declarative_base()

class PricingData(Base):
    __tablename__ = 'pricing_data'
    id = Column(String, primary_key=True)
    ticker = Column(String)
    datetime = Column(DateTime)
    open = Column(Numeric)
    high = Column(Numeric)
    low = Column(Numeric)
    close = Column(Numeric)

    def __repr__(self):
        return "<PricingData(ticker='%s', timestamp='%s', open='%s', high='%s', low='%s', close='%s')>" % (
            self.ticker, self.datetime, self.open, self.high, self.low, self.close)