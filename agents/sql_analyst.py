import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from utills.llm_pick import pick_llm
from Models.schema import AgentSchema

#---------------------------------------- AI Agent Code ---------------------------------------------------


def curate_question(state: AgentSchema) -> AgentSchema:

    user_question = state.user_question 
    llm = pick_llm("low")

    response = llm.invoke(f"Curate the following questoin: {user_question}")

    state.curated_ques = response
    return state

