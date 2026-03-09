from fastapi import FastAPI
from models_llm.RAG import qa_chain

app = FastAPI()

@app.get('/consultar_whatsapp/{pregunta:path}')
async def mensaje_whatsapp(pregunta: str):
    print('Pregunta recibida:', pregunta)
    try:     
        resultado = qa_chain.invoke({'query': pregunta})
        
        return {'respuesta': resultado['result']}
    
    except Exception as e:
        return {'respuesta:': f'Lo siento, hubo un error interno en: {str(e)}'}    

