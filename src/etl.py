from metaflow import FlowSpec, step
import pandas as pd
from sqlalchemy import create_engine
import logging

logging.basicConfig(level=logging.INFO)

class AirbnbETLFlow(FlowSpec):
    @step
    def start(self):
        self.next(self.load_data)

    @step
    def load_data(self):
        try:
            self.df = pd.read_csv('data/AB_NYC_2019.csv')
            logging.info(f"Data loaded successfully. Shape: {self.df.shape}")
            self.next(self.transform_data)
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            raise

    @step
    def transform_data(self):
        try:
            self.df['date'] = pd.to_datetime(self.df['last_review']).dt.date
            self.df['time'] = pd.to_datetime(self.df['last_review']).dt.time
            self.avg_price = self.df.groupby('neighbourhood_group')['price'].mean().reset_index()
            self.df['reviews_per_month'].fillna(0, inplace=True)
            self.df['price_per_person'] = self.df['price'] / self.df['minimum_nights']
            self.df['is_expensive'] = self.df['price'] > self.df['price'].median()
            logging.info("Data transformation completed successfully")
            self.next(self.load_to_db)
        except Exception as e:
            logging.error(f"Error in data transformation: {str(e)}")
            raise

    @step
    def load_to_db(self):
        try:
            engine = create_engine('postgresql://colab:colab@localhost/airbnb_db')
            self.df.to_sql('airbnb_data', engine, if_exists='replace', index=False, chunksize=1000)
            self.avg_price.to_sql('avg_price_by_neighborhood', engine, if_exists='replace', index=False)
            logging.info("Data loaded to database successfully")
            self.next(self.end)
        except Exception as e:
            logging.error(f"Error loading data to database: {str(e)}")
            raise

    @step
    def end(self):
        print("ETL process completed successfully!")

if __name__ == '__main__':
    AirbnbETLFlow()
