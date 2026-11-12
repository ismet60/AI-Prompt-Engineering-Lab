from langchain_groq import ChatGroq

# Set GROQ_API_KEY privately in your environment before running this file.
llm = ChatGroq(model="openai/gpt-oss-20b")

# The example does not provide actual company hours.
messages = [
    ("system", "You are a customer support representative. Your goal is to efficiently handle queries."),
    ("human", "What are your business hours?"),
]
result = llm.invoke(messages)
print(result.content)
