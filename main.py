from api.microservicio_rag import app

def start():
    import uvicorn
    uvicorn.run('api.microservicio_rag:app', host='0.0.0.0', port=5050, reload=True)

if __name__ == '__main__':
    start()
