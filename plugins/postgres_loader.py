from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load(data, table_name):
    user = 'airflow'
    passwd = 'airflow'
    hostname = 'postgres'  # Ensure this matches the service name in Docker Compose
    database = 'data_warehouse'   # Ensure this matches your database name

    conn_string = f'postgresql://{user}:{passwd}@{hostname}:5432/{database}'

    try:
        # Create an engine instance
        db = create_engine(conn_string)

        # Connect to the database
        with db.connect() as conn:
            # Load data into the specified table
            data.to_sql(table_name, con=conn, if_exists='append', index=False)
        
        logger.info("Successfully loaded to Postgres")

    except SQLAlchemyError as e:
        logger.error(f"An error occurred: {e}")

