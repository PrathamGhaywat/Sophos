from ollama import chat

def get_kw(text):
    """
    This function gets the appropriate keywords, simulating as if an actual human would be searching
    """
    keyword = chat(
        model='gemma3:1b',
        messages=[
            {'role':'system', 'content': 'You are a Keyword Specialist Core finder at a research institue. Your job is to provide the crucial keywords on the following prompt. Make sure to find the core defnition the user is trying to find out. Reply only with one keyword in plain text no markdown. Reply in such a manner, as if a normal person searching it on arxiv.org would.'},
            {'role': 'user', 'content': text}
    ]
    )
    return keyword['message']['content']

def model_ans(text : str, info : str):
    """
    This function fetches the response from the AI Model.
    """
    response = chat(
        model='gemma3:1b',
        messages=[
            {'role': 'system', 'content': "You are a Research Professor called Sophos. Your job is to assist users in conducting advanced research by answering questions, summarizing complex topics, suggesting methodologies, and referencing relevant academic material. You speak with clarity, precision, and a tone of intellectual curiosity. Use examples, analogies, and references where appropriate. When necessary, guide users to think critically and ask deeper questions. For your help you have these following research papers: " + info},
            {'role': 'user', 'content': text}
    ]
    )
    return response['message']['content']