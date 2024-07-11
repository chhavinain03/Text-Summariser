import os
from langchain import PromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.prompt_template import format_document
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI

def summarize(file):
    os.environ['GOOGLE_API_KEY'] = 'AIzaSyDGkSLsqjwLb5QNwl-U7hz0UHrnHGvMyS4'  

    # Load the PDF document
    loader = PyPDFLoader(file)
    docs = loader.load()

    # Set up the Google Generative AI model
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7, top_p=0.85)

    # Create a prompt template for extracting data from the documents
    doc_prompt = PromptTemplate.from_template("{page_content}")

    # Create a prompt template for querying Gemini
    llm_prompt_template = """Write a  summary  about 50-100 lines of the following:
    "{text}"
    CONCISE SUMMARY:"""
    llm_prompt = PromptTemplate.from_template(llm_prompt_template)

    # Define the chain to process the documents and get summaries
    stuff_chain = (
        # Extract data from the documents and add to the key `text`
        {
            "text": lambda docs: "\n\n".join(
                format_document(doc, doc_prompt) for doc in docs
            )
        }
        | llm_prompt         # Prompt for Gemini
        | llm                # Gemini function
        | StrOutputParser()  # Output parser
    )

    # Invoke the chain on the documents
    response = stuff_chain.invoke(docs)
    return response

def save_uploadedfile(uploadedfile):
    # Ensure the data directory exists
    if not os.path.exists("data"):
        os.makedirs("data")

    file_path = os.path.join("data", uploadedfile.filename)
    with open(file_path, "wb") as f:
        f.write(uploadedfile.read())
    return file_path
