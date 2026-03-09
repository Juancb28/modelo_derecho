from fastapi import APIRouter
from models.RAG import qa_chain

router = APIRouter()

@router.get('/consultar_whatsapp/{pregunta:path}', tags=['solicitud'])
async def mensaje_whatsapp(pregunta: str):
    print('Pregunta recibida:', pregunta)
    try:     
        resultado = qa_chain.invoke({'query': pregunta})
        
        return {'respuesta': resultado['result']}
    
    except Exception as e:
        return {'respuesta:': f'Lo siento, hubo un error interno en: {str(e)}'}    