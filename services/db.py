from azure.cosmos import CosmosClient

import config


client = CosmosClient(
    config.COSMOS_DATABASE['host'],
    credential=config.COSMOS_DATABASE['master_key']
)

container_name = config.COSMOS_DATABASE["container_id"]
database = client.get_database_client(config.COSMOS_DATABASE["database_id"])
container = database.get_container_client(config.COSMOS_DATABASE["container_id"])


class CosmosDatabase:

    @staticmethod
    def get_by_id(id_):
        query = f'SELECT * FROM {container_name} WHERE {container_name}.id = \'{id_}\''
        items = container.query_items(query, enable_cross_partition_query=True)
        for val in items:
            return val

        return None

    @staticmethod
    def put_item(data):
        return container.create_item(data)
