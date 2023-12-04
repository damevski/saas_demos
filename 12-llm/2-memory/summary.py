from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain  # Import LLMChain
from dotenv import load_dotenv
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationSummaryMemory

if __name__ == "__main__":
    load_dotenv()

    chat_model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)

    memory = ConversationSummaryMemory(llm=chat_model)

    prompt = PromptTemplate.from_template("You are a CS student. What is a good short title for a class on {topic}?")

    chain = LLMChain(
        llm=chat_model,
        prompt=prompt,
        verbose=True,  # Set verbose to True
        memory=memory
    )

    res = chain({"topic": "software as a service"})
    res = chain({"topic": "software testing"})
    res = chain({"topic": "software engineering"})
    res = chain({"topic": "programming languages"})

    print(res)