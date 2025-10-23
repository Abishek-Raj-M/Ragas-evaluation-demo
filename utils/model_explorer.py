"""
Model Explorer Utility for EPAM DIAL API
Contains functions to explore available models and deployments
"""

import os
import requests
from dotenv import load_dotenv

def load_api_config():
    """Load API configuration from .env file"""
    load_dotenv()
    
    api_key = os.getenv('DIAL_API_KEY')
    azure_endpoint = os.getenv('AZURE_ENDPOINT', 'https://ai-proxy.lab.epam.com')
    api_version = os.getenv('API_VERSION', '2024-02-01')
    
    if not api_key:
        raise ValueError("DIAL_API_KEY not found in .env file")
    
    return api_key, azure_endpoint, api_version

def get_available_models(api_key, azure_endpoint, api_version):
    """Fetch available models from Azure OpenAI"""
    headers = {
        'api-key': api_key,
        'Content-Type': 'application/json'
    }
    
    try:
        # Azure OpenAI models endpoint
        url = f"{azure_endpoint}/openai/deployments?api-version={api_version}"
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Models endpoint returned status {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching models: {e}")
        return None

def main():
    """Main function to explore EPAM DIAL API"""
    print("EPAM DIAL API Model Explorer")
    print("=" * 50)
    
    try:
        # Load configuration
        api_key, azure_endpoint, api_version = load_api_config()
        print(f"Azure Endpoint: {azure_endpoint}")
        print(f"API Version: {api_version}")
        print(f"API Key: {api_key[:10]}...{api_key[-10:]}")
        print()
        
        # Get available models
        print("Fetching available deployments...")
        models_data = get_available_models(api_key, azure_endpoint, api_version)
        
        if models_data:
            deployments = models_data.get('data', [])
            print(f"Found {len(deployments)} available deployments:")
            print()
            
            # Analyze each deployment
            llm_deployments = []
            embedding_deployments = []
            
            for deployment in deployments:
                deployment_name = deployment.get('id', 'unknown')
                model_name = deployment.get('model', 'unknown')
                
                print(f"Deployment: {deployment_name}")
                print(f"  Model: {model_name}")
                print(f"  Status: {deployment.get('status', 'unknown')}")
                
                # Determine if it's suitable for LLM or embeddings
                is_llm = any(keyword in model_name.lower() for keyword in [
                    'gpt', 'claude', 'llama', 'text-davinci', 'chat'
                ])
                
                is_embedding = any(keyword in model_name.lower() for keyword in [
                    'embedding', 'ada', 'text-embedding'
                ])
                
                print(f"  Suitable for LLM: {is_llm}")
                print(f"  Suitable for Embeddings: {is_embedding}")
                print()
                
                if is_llm:
                    llm_deployments.append(deployment_name)
                if is_embedding:
                    embedding_deployments.append(deployment_name)
            
            # Recommendations
            print("RAGAS Evaluation Recommendations:")
            print("-" * 40)
            
            if llm_deployments:
                print(f"Recommended LLM Deployment: {llm_deployments[0]}")
            else:
                print("No suitable LLM deployments found")
            
            if embedding_deployments:
                print(f"Recommended Embedding Deployment: {embedding_deployments[0]}")
            else:
                print("No dedicated embedding deployments found - may need to use LLM for embeddings")
            
        else:
            print("Could not fetch deployments.")
    
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure your .env file contains:")
        print("DIAL_API_KEY=your_api_key_here")
        print("AZURE_ENDPOINT=https://ai-proxy.lab.epam.com")
        print("API_VERSION=2024-02-01")

if __name__ == "__main__":
    main()
