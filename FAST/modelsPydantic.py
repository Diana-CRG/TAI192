from pydantic import BaseModel, Field, EmailStr, field_validator

#Modelo de validaciones
class modelusuario(BaseModel):
    id:int = Field(...,gt=0, description="id unico y solo numeros positivos")
    nombre:str = Field(...,min_length=3, max_length=85, description="Letras entre 3 y 85")
    edad:int = Field(..., ge=18, le=100, description="Debe ser un número entre 18 y 100")
    correo: EmailStr = Field(..., description="Debe ser un correo válido")

    @field_validator("email")
    @classmethod
    def validar_dominio_correo(cls, value):
        dominio_permitido = "@solidareco.com.mx"
        if not value.endswith(dominio_permitido):
            raise ValueError(f"El correo debe pertenecer al dominio {dominio_permitido}")
        return value
    

#creacion de modelo
class modeloAuth(BaseModel):
    email: EmailStr = Field(..., description="Correo valido", example="correo@example.com")
    passw: str = Field(..., min_lenght=8, strip_whitespace=True, description="Contraseña con minimo 8 caracteres")
        