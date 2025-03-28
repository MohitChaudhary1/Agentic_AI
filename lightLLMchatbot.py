from smolagents import CodeAgent, LiteLLMModel

model= LiteLLMModel("openai/gpt-4o",temprature=0.2)

messages=[]

while True:
    user_input=input("Enter a Message")
    if user_input=="exit":
        break

    messages.append({"role":"user", "content":user_input})

    response=model(messages, max_token=500)
    assistant_message=response.content

    print("Assistant:",assistant_message)
    messages.append({"role":"assistant","content":assistant_message})