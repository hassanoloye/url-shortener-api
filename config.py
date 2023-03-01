import os
import dotenv

dotenv.load_dotenv()

COSMOS_DATABASE = {
    'host': os.environ.get('COSMOS_DATABASE_HOST'),
    'master_key': os.environ.get('COSMOS_DATABASE_KEY'),
    'database_id': os.environ.get('COSMOS_DATABASE_NAME'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}