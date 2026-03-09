from models_llm.RAG import qa_chain



def query(pregunta: str):
    # pregunta = '''
    # Soy estudiante de derecho y quiero saber sobre el procedimiento 
    # cuando existe una muerte, necesito saber especificamente sobre el juez
    # '''
    resultado = qa_chain.invoke({'query': pregunta})

    print(f"\n Respuesta: {resultado['result']}")
    

if __name__ == '__main__':
    query()