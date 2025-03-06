from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from genToken import validateToken


class BearerJWT(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)

        data = validateToken(auth.credentials)

        if not isinstance(data, dict): #verificar que si es un diccionario valido
            raise HTTPException(status_code=401, detail="token invalido")
        
        if data.get('email') != 'diana@example.com':  #usar .get() para evitar KeyError
            raise HTTPException(status_code=403, detail="Credenciales no validas")