def build_prompt(content_chunks, query):
    content = "\n\n".join(content_chunks)
    return f"""Use the follwoing content to answer the question.

    Context:{content}

    Question:{query}
    
    Answer:
    """