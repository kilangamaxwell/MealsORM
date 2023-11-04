from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the data table class's parent class
Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    restaurant_id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_name = Column(String)
    restaurant_city = Column(String)
    famous_dish = Column(String)

    def __repr__(self):
        return f"Restaurant(restaurant_id = {self.restaurant_id}, name = {self.restaurant_name})"

# Create a database connection
engine = create_engine('sqlite:///restaurants.sqlite')

# Create a database session
Session = sessionmaker(bind=engine)
session = Session()
