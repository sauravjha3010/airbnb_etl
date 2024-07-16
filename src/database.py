from sqlalchemy import create_engine, text
import pandas as pd

def query_database():
    engine = create_engine('postgresql://colab:colab@localhost/airbnb_db')

    # Query the airbnb_data table
    query = text("SELECT * FROM airbnb_data LIMIT 5")
    result = pd.read_sql(query, engine)
    print("Sample data from airbnb_data table:")
    print(result)

    # Query the avg_price_by_neighborhood table
    query = text("SELECT * FROM avg_price_by_neighborhood")
    result = pd.read_sql(query, engine)
    print("\nAverage price by neighborhood:")
    print(result)

if __name__ == "__main__":
    query_database()
