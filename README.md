# Airbnb New York City ETL Pipeline

This project implements a scalable ETL (Extract, Transform, Load) pipeline for the Airbnb New York City dataset using Python, PostgreSQL, and Metaflow.

## Project Overview

The ETL pipeline performs the following tasks:
1. Extracts data from a CSV file
2. Transforms the data (normalizes dates, calculates metrics, handles missing values)
3. Loads the transformed data into a PostgreSQL database
4. Uses Metaflow to manage the ETL workflow

## Installation

1. Clone this repository:
git clone https://github.com/yourusername/airbnb_etl.git
cd airbnb_etl
Copy
2. Install the required packages:
pip install -r requirements.txt
Copy
3. Set up PostgreSQL database:
- Install PostgreSQL
- Create a database named `airbnb_db`
- Update the database connection string in `src/etl.py` and `src/database.py` if necessary

## Usage

1. Place the Airbnb dataset (`AB_NYC_2019.csv`) in the `data/` directory.

2. Run the ETL pipeline:
python -m metaflow run src/etl.py
Copy
3. Query the database:
python src/database.py
Copy
## ETL Process

1. Data Extraction: The data is extracted from the CSV file using pandas.
2. Data Transformation:
- Date and time are separated into different columns
- Average price per neighborhood is calculated
- Missing values in 'reviews_per_month' are filled with 0
- New metrics like 'price_per_person' and 'is_expensive' are calculated
3. Data Loading: The transformed data is loaded into PostgreSQL tables

## Database Schema

- airbnb_data: Contains all columns from the original dataset plus the new transformed columns
- avg_price_by_neighborhood: Contains average price for each neighborhood group

## Metaflow Workflow

The Metaflow workflow consists of the following steps:
1. start
2. load_data
3. transform_data
4. load_to_db
5. end

To visualize the Metaflow graph, run:
python -m metaflow show AirbnbETLFlow
Copy
## Future Improvements

- Implement data quality checks
- Add more complex transformations
- Optimize database schema for better query performance
- Implement incremental loading for handling larger datasets

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
