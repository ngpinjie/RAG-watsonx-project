import os
from dotenv import load_dotenv
from genai.extensions.langchain import LangChainInterface
from genai.schemas import GenerateParams
from genai.credentials import Credentials
from langchain.chains import RetrievalQA

# Load environment variables
load_dotenv()
api_key = os.getenv("GENAI_KEY")
api_url = os.getenv("GENAI_API")

# Set credentials
creds = Credentials(api_key, api_endpoint=api_url)

# Define the model and parameters
model_id = "meta-llama/llama-2-70b-chat"
params = GenerateParams(
    decoding_method="greedy",
    max_new_tokens=1000,
    min_new_tokens=200,
    temperature=0.7,
)

# Create the LangChain interface
llm = LangChainInterface(model=model_id, params=params, credentials=creds)

# Assuming load_pdf.py has already run and index is created
from load_pdf import load_pdf
index = load_pdf()

# Set up the retrieval-based QA chain
chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=index.vectorstore.as_retriever(),
    input_key='question'
)

# Run a query
response = chain.run("PROMPT OPTIMIZATION EXPERIMENTS results?")
print(response)
