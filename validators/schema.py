from pydantic import BaseModel, HttpUrl, validator, ValidationError


class URL(BaseModel):
    value: HttpUrl


class ShortenRequest(BaseModel):
    url: str

    @validator('url')
    def valid_url(cls, value):
        try:
            parsed_value = value if value.startswith('http://') or value.startswith('https://') else f'http://{value}'
            URL(value=parsed_value)
            return value
        except ValidationError as e:
            raise ValueError('Not a valid url')
