from fastapi import FastAPI, HTTPException

from cache import Cache
from services.token import TokenService
from services.shortener import ShortenerService
from validators.schema import ShortenRequest

app = FastAPI()


@app.get("/{key}")
async def get_url(key: str):
    # TODO: Cache value returned from the database
    cached_value = Cache.get(key)
    if cached_value is not None:
        return {"key": key, "url": cached_value}

    record = ShortenerService.get(key)
    if record is None:
        raise HTTPException(status_code=400, detail="key does not exist")

    return {"key": record["id"], "url": record["url"]}


@app.post("/")
async def shortener(payload: ShortenRequest):
    key = TokenService.generate()

    ShortenerService.store(key, payload.url)
    Cache.set(key, payload.url)

    return {"key": key, "url": payload.url}
