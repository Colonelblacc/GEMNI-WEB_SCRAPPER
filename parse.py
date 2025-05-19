
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

import getpass
import os





template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key="AIzaSyCGJrbm-QVYnCQIzJ96uCMX_-VWmTaiV7c",
    temperature=0.7
)

def parse_with_gemini(dom_chunks,parse_description):
    prompt= ChatPromptTemplate.from_template(template)
    chain=prompt|llm

    parsed_results=[]
    for i, chunk in enumerate(dom_chunks,start=1):
        response=chain.invoke(
            {"dom_content":chunk,"parse_description":parse_description}
        ) 
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        text_response = response.content  
        parsed_results.append(text_response)

    return "\n".join(parsed_results)    
