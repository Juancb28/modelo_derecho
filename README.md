# Librerias

Instalación -> pip install langchain-community pypdf qdrant-client sentence-transformers

```
from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    url="https://5a4ef37b-f9a7-4f34-914e-fdbe1d67f71e.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.AsZLsQQkB3SLbbg_8Gc8G-o3f2vPQtJfp-Gxsla9V8g",
)

print(qdrant_client.get_collections())
```
