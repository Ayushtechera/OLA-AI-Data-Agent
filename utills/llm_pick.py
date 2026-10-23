from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()



def pick_llm(level: str):
    """
    Picks the appropriate LLM based on the lvel of the question.

    Args:
        level (str): The level of the question, can be "easy", "medium", or "hard".

    Return:
        str: The name of the LLM to be used.
    """


    if level.lower() == "low":
        llm = ChatGroq(
            model="openai/gpt-oss-20b",
            temperature=0
        )
    elif level.lower() == "medium":
        llm = ChatGroq(
            model="qwen/qwen3.8-27b",
            temperature=0
        )
    elif level.lower() == "high":
        llm = ChatGroq(
            model="openai/gpt-oss-120b",
            temperature=0
        )
    else:
        raise ValueError(f"Unsupported level: {level}")

    return llm


