from pydantic import BaseModel, Field, EmailStr, field_validator

#Modelo de validaciones
from pydantic import BaseModel, Field, EmailStr, field_validator

class modelusuario(BaseModel):
    name: str = Field(..., min_length=3, max_length=85, description="Debe tener entre 3 y 85 caracteres")
    age: int = Field(..., ge=18, le=100, description="Debe ser un número entre 18 y 100")
    email: EmailStr = Field(..., description="Debe ser un correo válido")

    @field_validator("email")
    @classmethod
    def validar_dominio_correo(cls, value):
        dominio_permitido = "@gmail.com"
        if not value.endswith(dominio_permitido):
            raise ValueError(f"El correo debe pertenecer al dominio {dominio_permitido}")
        return value

    

#creacion de modelo
class modeloAuth(BaseModel):
    email: EmailStr = Field(..., description="Correo válido", example="correo@gmail.com")
    passw: str = Field(..., min_length=8, strip_whitespace=True, description="Contraseña con mínimo 8 caracteres")
