import secrets


class TokenService:

    @staticmethod
    def generate():
        return secrets.token_urlsafe(5)
