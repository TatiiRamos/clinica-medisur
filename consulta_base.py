from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv , find_dotenv
import os
import openai
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

# Cargar variables de entorno
load_dotenv(find_dotenv())

# Ensure the API key is loaded from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("❌ ERROR: No se encontró la clave OPENAI_API_KEY. Verifica tu archivo .env y reinicia la terminal.")

# Crear el objeto OpenAIEmbeddings con la API Key
emb = OpenAIEmbeddings(openai_api_key=openai.api_key)

emb = OpenAIEmbeddings()
BASE = Chroma (persist_directory="base", 
                embedding_function=emb)


# print (BASE.get())

# busqueda semantica
def busqueda_semantica(pregunta, k=5):
    res = ""
    fragmentos = BASE.max_marginal_relevance_search(pregunta, k=5)
    for doc in fragmentos:
        res += f"Fuente : {doc.metadata['source']}\n" 
        res += doc.page_content + "\n\n"
    return res


if __name__ == "__main__": 
    pregunta = input (">>>")
    # vamos a traer los 5 fragmentos mas relevantes para una pregunta

    contexto = busqueda_semantica(pregunta, k=5)
    print(contexto)
    
    # for i, doc in enumerate(fragmentos):
    #     print("fragmento Nº:" , i)
    #     print(doc.metadata["source"])
    #     print(fill(doc.page_content,80))