from services.db import CosmosDatabase


class ShortenerService:

    @staticmethod
    def get(key):
        return CosmosDatabase.get_by_id(key)

    @staticmethod
    def store(key, url):
        return CosmosDatabase.put_item({
            "id": key,
            "url": url
        })
