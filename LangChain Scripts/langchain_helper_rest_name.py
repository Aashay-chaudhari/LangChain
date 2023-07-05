from langchain import LLMChain
from langchain.chains import SequentialChain
from langchain.llms import OpenAI
import os

from langchain.prompts import PromptTemplate


def generate_name_and_items(cuisine):
    os.environ['OPENAI_API_KEY'] = ""
    llm = OpenAI(temperature=1)

    propmt_template_name = PromptTemplate(
        input_variables=["cuisine", "diet"],
        template="I want to open an restaurant for {diet} {cuisine} food. Suggest a fancy name for this restaurant."
    )

    name_chain = LLMChain(llm=llm, prompt=propmt_template_name, output_key="rest_name")

    propmt_template_items = PromptTemplate(
        input_variables=["rest_name"],
        template="Suggest top 3 dishes for the restaurant {rest_name} with their description. Return these items and descriptions seperated by a $."
    )

    items_chain = LLMChain(llm=llm, prompt=propmt_template_items, output_key="menu_items")

    prompt_template_promotions = PromptTemplate(
        input_variables=["menu_items"],
        template="Suggest 3 promotional offers for each of the menu items: {menu_items}."
    )

    promo_chain = LLMChain(llm=llm, prompt=prompt_template_promotions, output_key="promos")

    chain = SequentialChain(
        chains=[name_chain, items_chain, promo_chain],
        input_variables=["cuisine", "diet"],
        output_variables=["rest_name", "menu_items", "promos"]
    )
    resp = chain({"cuisine": cuisine, "diet": "non-veg"})
    print("resp is: ", resp)
    return {
        "rest_name": resp['rest_name'],
        "menu_items": resp['menu_items'],
        "promos": resp['promos']
    }
