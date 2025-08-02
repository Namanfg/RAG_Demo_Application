import pickle

def chunking(raw_text,max_words=150):
    words = raw_text.split()
    chunks = []
    for i in range(0,len(words),max_words):
        chunks.append(" ".join(words[i:i+max_words]))
    file_name = 'chunks.pkl'
    with open(file_name,'wb') as file:
        pickle.dump(chunks,file)
    return chunks