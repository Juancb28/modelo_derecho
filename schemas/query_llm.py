from models.RAG import qa_chain
import solicitud


def query(solicitud: solicitud):
    resultado = qa_chain.invoke({"query": solicitud})
    print(f"\n Respuesta: {resultado['result']}")


if __name__ == "__main__":
    query()
