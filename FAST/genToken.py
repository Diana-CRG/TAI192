import jwt
from  jwt import ExpiredSignatureError, InvalidTokenError
from fastapi import HTTPException

#Generar token
def createToken(datos:dict):
    token:str = jwt.encode(payload=datos, key='secretkey', algorithm='HS256')
    return token

def validateToken(token: str):
    try:
        datos: dict = jwt.decode(token, key='secretkey', algorithm=['HS256'])  # Cambia 'algorithm' a 'algorithms'
        return datos
    except ExpiredSignatureError:
        raise HTTPException(status_code=403, detail='Token expirado')
    except InvalidTokenError:
        raise HTTPException(status_code=403, detail='Token no autorizado')

    