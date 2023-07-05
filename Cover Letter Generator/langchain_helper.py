from langchain import LLMChain
from langchain.llms import OpenAI
import os

from langchain.prompts import PromptTemplate


def generate_cover_letter(requirements):
    print("Inside gen cover letter")
    os.environ['OPENAI_API_KEY'] = ""
    llm = OpenAI(model_name='gpt-3.5-turbo-16k', temperature=0)
    print("requirements are: ", requirements)
    print("llm assigned using open ai key")
    propmt_template_cover = PromptTemplate(
        input_variables=["requirements"],
        template="This is my resume:          Aashay Chaudhari         Phone: +1(513) 957-9982 | "
                 "Email:chaudha7@mail.uc.edu          LinkedIn GitHub Website         Summary          Machine "
                 "Learning professional with a Master's Degree in ML and over 2 years of industry experience.         "
                 "Education          Meng in Artificial Intelligence/Machine Learning University of Cincinnati "
                 "Aug-2022– Aug 2023           Bachelor of Engineering, Information Technology Pune University July "
                 "2017 – May 2021           Work Experience         Fantail Consulting and Technologies – Machine "
                 "Learning Engineer Intern May 2023 to Present         • Researched, finetuned and deployed "
                 "pretrained LLM models on Hugging Face Inference API.         • Innovated LLM solutions for private "
                 "organisations with propriety data.         • Engineered a solution for summarization and "
                 "document-based QA around OpenAI LLMs.         • Tech Stack: MLOps (Azure ML, KubeFlow, Hugging Face "
                 "Inference, LangChain), Versioning (MLflow, GitHub),          Databases (SQL, Neo4j, Pinecone)       "
                 "  Fantail Consulting and Technologies – Full Stack Developer (ML) Jun 2021 to Jun 2022         • "
                 "Designed a document tagging and search retrieval system using vector databases and cosine "
                 "similarities.         • Responsible for front end feature integration, backend implementation and "
                 "optimization, API management          and production deployment of 2 (ceir, qbs) complex Angular "
                 "applications.         • Tech Stack: Frontend Frameworks (Angular, Django), Ops (Docker, "
                 "AWS: Lambda, API and Cognito), Databases          (MySQL, Pinecone, Neo4j), Backend Frameworks ("
                 "Django Rest Framework, SpringBoot)          Krushiark Naturals – Machine Learning Engineer May 2020 "
                 "to May 2021         • Developed various complex regression models (stacked LSTMs, Time series "
                 "optimized Transformers) for sales          forecasting and trend identification, which led to "
                 "better inventory preparation.         • Developed an advanced targeted marketing system that "
                 "utilized statistical methods to recommend products         to users based on their website "
                 "behaviour, leveraging data collected through Google Analytics.         • Tech Stack: MLOps (AWS "
                 "EC2, Docker), Versioning (Bitbucket, GitHub Actions, MLflow), Databases (MySQL)         Technical "
                 "Skills          Programming Languages -> Python, Java, C++          Frameworks -> Angular, "
                 "Django (Rest + Web) Framework, Flask, FastAPI, LangChain          Operation Tools -> MLflow, "
                 "Docker, Kubernetes, Azure ML, KubeFlow          Versioning and DB -> GitHub, GitHub Actions, "
                 "Bitbucket, MySQL (Complex JOINS and Nested queries), Neo4j          Research Papers – Stock Price "
                 "Prediction using GRU, SimpleRNN and LSTM         Projects         • Created TradeSense (A website "
                 "that utilizes advanced machine learning algorithms to generate buy and sell signals)         ➔ "
                 "Signals provided by the platform are consistently profitable on a monthly basis. Refer these "
                 "notebooks for back          testing and accuracy results.         ➔ Platform provides "
                 "state-of-the-art historic chart pattern matching functionality using complex clustering algorithms. "
                 "        • Stock Management Software (Created a stock management software for retailers that exposes "
                 "data through API)         ➔ Integration with powerful regression analysis tools to predict sales of "
                 "a particular territory and inventory          management.         • EDA Projects         ➔ COVID 19 "
                 "(Analysing distributions over different factors like Age, Gender, Nationality, "
                 "Type of Transmission, etc)         ➔ Data Scientist Salaries (Analysing distributions over "
                 "Experience, Company Location and Size, Job Title, etc)         ➔ Adult Income Dataset (Analysing "
                 "distributions over Age, Race, Sex, Marital Status, Hours/week, etc)         • Deep "
                 "Learning/Transformer based Models         ➔ Image-data based Models: DenseNet, GoogleNet, "
                 "MobileNet, ShuffleNet, VGG + Multilayered CNN         ➔ Time-series based Models: VAE and GANs, "
                 "Univariate, Bivariate, Attention + Transformer         ➔ NLP-based Models: TF-IDF, Neural Network, "
                 "LSTMs, Word Embedding + Transformer         ➔ LLM Finetuning and Research: Falcon 40b, Flan t5 XXL, "
                 "MPT Models, Nous Hermes 13b, Minotaur 13b                  These are the job requirements:          "
                 "         {requirements}                  Please write me a cover letter that showcases my "
                 "experience relating to the job requirements and explains to the hiring          manager why I am a "
                 "good candidate for this position. Return the name of the company I'm applying to and cover letter in the form"
                 "of dictionary having cover_letter and company_name "
    )
    print("prompt template done. ")
    chain = LLMChain(llm=llm, prompt=propmt_template_cover)
    print("chain created")
    resp = chain.run(requirements)

    print("response is: ", resp)

    return resp
