from fastapi import FastAPI
from models_llm.RAG import qa_chain

app = FastAPI()

@app.get('/consultar_whatsapp/{pregunta}')
async def mensaje_whatsapp(pregunta: str):
    
    try:     
        resultado = qa_chain.invoke({'query': pregunta})
        
        return {'respuesta:': resultado['result']}
    
    except Exception as e:
        return {f'respuesta:' : 'Lo siento, hubo un error interno en: {str{e}}'}    

