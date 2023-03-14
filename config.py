import os
import dotenv

dotenv.load_dotenv()

COSMOS_DATABASE = {
    'host': os.environ.get('COSMOS_DATABASE_HOST'),
    'master_key': os.environ.get('COSMOS_DATABASE_KEY'),
    'database_id': os.environ.get('COSMOS_DATABASE_NAME'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}
ENVIRONMENT = os.environ.get('ENVIRONMENT')

if ENVIRONMENT == 'local':
    origins = [
        "http://localhost:3000",
    ]
else:
    origins = [
        "https://fasturlshortener.azurewebsites.net",
        "https://www.fasturlshortener.azurewebsites.net",
        "https://zealous-ocean-085c2dc10.2.azurestaticapps.net"
    ]
