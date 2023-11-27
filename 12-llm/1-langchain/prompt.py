from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate


 
if __name__ == "__main__":
    load_dotenv()

    chat_model = ChatOpenAI(model_name="gpt-3.5-turbo")

    prompt = PromptTemplate.from_template("You are a CS student. What is a good short title for a class on {topic}?")
    text = prompt.format(topic="software as a service")

    messages = [HumanMessage(content=text)]
    res = chat_model.invoke(messages)

    print(res)



