from models_llm.RAG import qa_chain



def query():
    pregunta = 'Para que la tradición sea válida debe ser hecha voluntariamente por el tradente o por su representante. Es correcto?'
    resultado = qa_chain.invoke({'query': pregunta})

    print(f"\n Respuesta: {resultado['result']}")
    

if __name__ == '__main__':
    query()