import openai

#pull openai api key from hidden/secure location
openai.api_key = open("openai_creds.gitignore","r").read().strip()

message_history = []
    
def chat(user_input, role="user"):
    """Begin user:assistant conversation loop  
    """

    #message history is stored in the chat completion create api call
    message_history.append({"role": role, "content": f"{user_input}"})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )
    reply = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": f"{reply}"})
    return reply
