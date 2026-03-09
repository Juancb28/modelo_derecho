from pydantic import BaseModel

class solicitud(BaseModel):
    id: int
    pregunta: str
    

def guardar_solicitud(item) -> dict:
    return {
        'id': str(item.id),
        'solicitud': str(item.pregunta)
    }