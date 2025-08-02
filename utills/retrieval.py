import faiss
import numpy as np 
import pickle
import os 
from utills.embedding import text_to_embedding
from utills.chunking import chunking

def load_faiss_index():
    if os.path.exists('faiss_store/index.faiss'):
        index = faiss.read_index("faiss_store/index.faiss")
        with open("faiss_store/chunks.pkl",'rb') as file:
            chunk_mapping = pickle.load(file)
    else:
        with open("data/data.txt","r",encoding="utf-8") as file:
            raw_text = file.read()
        
        chunks = chunking(raw_text=raw_text)
        chunk_mapping = []
        index = faiss.IndexFlatL2(3072)
        for chunk in chunks:
            emb = text_to_embedding(chunk)
            index.add(np.array([emb]).astype("float32"))
            chunk_mapping.append(chunk)
        os.makedirs("faiss_store",exist_ok=True)
        faiss.write_index(index,"faiss_store/index.faiss")
        with open("faiss_store/chunks.pkl",'wb') as file:
            pickle.dump(chunk_mapping,file)
    return index, chunk_mapping


def retrive_chunks(query,index,chunk_mapping,k=3):
    query_vec = text_to_embedding(query)
    D, I = index.search(np.array([query_vec]).astype("float32"),k)
    return [chunk_mapping[i] for i in I[0]]
