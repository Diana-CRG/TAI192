
from pydantic import BaseModel, Field

#Modelo de validaciones
class modelConductor(BaseModel):
    
    nombre:str = Field(...,min_length=3, max_length=85, description="Letras entre 3 y 85")
    tipoLicencia:str = Field(...,description="Debe ser solo 1 caracter y es entre A,B,C,D")
    NLicencia:int = Field(...,min_length=12, max_length=12, description="Debe tener 12 carcateres")
