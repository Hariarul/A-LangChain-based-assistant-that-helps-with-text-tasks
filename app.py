from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from tools.tools import get_profile_url_serpapi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tools import Tool
import os
from dotenv import load_dotenv
from third_parties.linkdin import scrape_linkedin_profile

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

def ice_breaker_with(name:str):
    linkedin_username = linkedin_lookup_agent(name=name)

    summary_template = """
    give me the Linkedin information {information}about a person I want to create:
    1.a short summary
    2. two interesting facts about them"""


    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

#llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
#llm = ChatOllama(model='gemma:2b')
    llm = ChatOllama(model='gemma:2b')

    output_parser = StrOutputParser()

    chain = summary_prompt_template | llm | output_parser
    res = chain.invoke(input={"information":information})
    print(res)

# load_dotenv()
# api_key = os.getenv("API_KEY")
# print(api_key)

# linkedin_data = scrape_linkedin_profile(Linkedin_profile_url="http://linkedin.com/in/haribaskar-a-a56045301")

# information = linkedin_data


# summary_template = """
# give me the Linkedin information {information}about a person I want to create:
# 1.a short summary
# 2. two interesting facts about them"""


# summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

# #llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
# #llm = ChatOllama(model='gemma:2b')
# llm = ChatOllama(model='gemma:2b')

# output_parser = StrOutputParser()

# chain = summary_prompt_template | llm | output_parser

if __name__=="__main__":
    print("Hello haribaskar welcome to learn langchain")
    ice_breaker_with(name="Haribaskar A")



    #res = chain.invoke(input={"information":information})

    #print(res.content)
    #print(res)

