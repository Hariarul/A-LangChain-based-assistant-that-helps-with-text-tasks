from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
print(api_key)

information = """
Cristiano Ronaldo dos Santos Aveiro (Portuguese pronunciation: [kɾiʃˈtjɐnu ʁɔˈnaldu] ⓘ; born 5 February 1985) is a Portuguese professional footballer who plays as a forward for and captains both Saudi Pro League club Al-Nassr and the Portugal national team. Nicknamed CR7, he is widely regarded as one of the greatest players in history, and has won numerous individual accolades throughout his professional footballing career, including five Ballon d'Or awards, a record three UEFA Men's Player of the Year Awards, four European Golden Shoes, and was named five times the world's best player by FIFA.[note 3] He has won 34 trophies in his career and holds numerous records, including most goals (140) in the UEFA Champions League, most goals (14) in the UEFA European Championship, and most international goals (138). He has made over 1,200 professional career appearances, the most by an outfield player, and has scored over 900 official senior career goals for club and country, making him the top goalscorer of all time.

Ronaldo began his career with Sporting CP before signing with Manchester United in 2003. He became a star player at United, where he won three consecutive Premier League titles, the Champions League, and the FIFA Club World Cup. His 2007–08 season earned him his first Ballon d’Or at age 23. In 2009, Ronaldo became the subject of the then-most expensive transfer in history when he joined Real Madrid in a deal worth €94 million (£80 million). At Madrid, he was at the forefront of the club’s resurgence as a dominant European force, helping them win four Champions Leagues between 2014 and 2018, including the long-awaited La Décima. He also won two La Liga titles, including the record-breaking 2011–12 season in which Madrid reached 100 points. He won Ballon d’Ors in 2013, 2014, 2016 and 2017 and became the club's all-time top goalscorer. Following issues with the club hierarchy, Ronaldo signed for Juventus in 2018, where he was pivotal in winning two Serie A titles. In 2021, he returned to United before joining Al-Nassr in 2023.
"""


summary_template = """
give me an information {information}about a person I want to create:
1.a short summary
2. two interesting facts about them"""


summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

#llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
llm = ChatOllama(model='gemma:2b')
#llm = ChatOllama(model='mistral')

output_parser = StrOutputParser()

chain = summary_prompt_template | llm | output_parser

if __name__=="__main__":
    print("Hello haribaskar welcome to learn langchain")



    res = chain.invoke(input={"information":information})

    #print(res.content)
    print(res)

