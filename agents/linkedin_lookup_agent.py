import os
from dotenv import load_dotenv
#from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import(create_react_agent,AgentExecutor)
from langchain import hub
from langchain_ollama import ChatOllama
from tools.tools import get_profile_url_serpapi
from serpapi import GoogleSearch
load_dotenv()


def lookup(name:str):
    llm = ChatOllama(model='gemma:2b')
    template = """Given the name "{name_of_person}", find their LinkedIn profile URL using the available tools. Do not answer directly. Use the tool to find the correct result."""

    prompt_template = PromptTemplate(template=template, input_variables=['name_of_person'])

    tools_for_agent = [
        Tool(
            name = "Crawl google 4 linkedin page",
            func= get_profile_url_serpapi, 
            description = "useful for when you need to get linkedin url"
        )
    ]
    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(llm=llm, tools = tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True,handle_parsing_errors=True)

    result = agent_executor.invoke(
        input={'input':prompt_template.format_prompt(name_of_person=name)}
    )

    linked_profile_url = result["output"]
    return linked_profile_url
    #return "http://linkedin.com/in/haribaskar-a-a56045301"

if __name__=="__main__":
    linkedin_url = lookup(name="haribaskar")
    print(linkedin_url)