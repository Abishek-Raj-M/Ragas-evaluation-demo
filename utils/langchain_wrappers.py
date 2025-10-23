"""
LangChain Wrappers for EPAM DIAL Models
Contains functions to create LangChain-compatible LLM and embedding models
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

def load_api_config():
    """Load API configuration from .env file"""
    load_dotenv()
    
    api_key = os.getenv('DIAL_API_KEY')
    azure_endpoint = os.getenv('AZURE_ENDPOINT', 'https://ai-proxy.lab.epam.com')
    api_version = os.getenv('API_VERSION', '2024-02-01')
    
    if not api_key:
        raise ValueError("DIAL_API_KEY not found in .env file")
    
    return api_key, azure_endpoint, api_version

def create_langchain_llm(deployment_name="gpt-4.1-mini-2025-04-14"):
    """
    Create a LangChain ChatOpenAI wrapper for EPAM DIAL LLM
    
    Args:
        deployment_name: The deployment name to use (default: gpt-4.1-mini-2025-04-14)
    
    Returns:
        ChatOpenAI: LangChain-compatible LLM wrapper
    """
    api_key, azure_endpoint, api_version = load_api_config()
    
    # Use the exact URL format that works
    base_url = f"{azure_endpoint}/openai/deployments/{deployment_name}"
    
    langchain_llm = ChatOpenAI(
        model=deployment_name,
        temperature=0.1,  # Low temperature for consistent evaluation
        max_tokens=1000,  # Reasonable limit for evaluation tasks
        n=1,  # Force single completion (required for EPAM DIAL)
        api_key=api_key,
        base_url=base_url,
        default_headers={
            "api-key": api_key,
            "api-version": api_version
        }
    )
    
    return langchain_llm

def create_langchain_embeddings(deployment_name="text-embedding-3-small-1"):
    """
    Create a LangChain OpenAIEmbeddings wrapper for EPAM DIAL embeddings
    
    Args:
        deployment_name: The deployment name to use (default: text-embedding-3-small-1)
    
    Returns:
        OpenAIEmbeddings: LangChain-compatible embedding wrapper
    """
    api_key, azure_endpoint, api_version = load_api_config()
    
    # Use the exact URL format that works
    base_url = f"{azure_endpoint}/openai/deployments/{deployment_name}"
    
    langchain_embeddings = OpenAIEmbeddings(
        model=deployment_name,
        api_key=api_key,
        base_url=base_url,
        default_headers={
            "api-key": api_key,
            "api-version": api_version
        }
    )
    
    return langchain_embeddings

if __name__ == "__main__":
    print("LangChain Wrappers Ready for RAGAS!")
    print("Use create_langchain_llm() and create_langchain_embeddings() in your RAGAS evaluation.")