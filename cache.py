from collections import OrderedDict

memory = OrderedDict()


class Cache:

    max_items = 100

    @staticmethod
    def build_key(key, prefix=None):
        if prefix is None:
            prefix = f'url_shortener_key:{key}'

        return prefix

    @staticmethod
    def set(key, value):
        cache_key = Cache.build_key(key)

        if cache_key not in memory and Cache.max_items <= len(memory):
            memory.popitem(last=False)

        memory[cache_key] = value

    @staticmethod
    def get(key):
        cache_key = Cache.build_key(key)

        return memory.get(cache_key)
