import os
from openai import OpenAI, AzureOpenAI
from prompt_chains import SYSTEM_PROMPT, build_user_prompt, SplunkTAConfig

def get_client():
    """Factory to return either an OpenAI or AzureOpenAI client based on ENV."""
    azure_key = os.getenv("AZURE_OPENAI_API_KEY")
    
    if azure_key:
        print("☁️  Using Azure OpenAI Service...")
        return AzureOpenAI(
            api_key=azure_key,
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-12-01-preview"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )
    else:
        print("🤖 Using standard OpenAI API...")
        return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ta_code(api_spec: str) -> SplunkTAConfig:
    client = get_client()
    
    # Determine which model/deployment name to use
    model_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME") or os.getenv("OPENAI_MODEL", "gpt-4o")
    
    try:
        response = client.beta.chat.completions.parse(
            model=model_name,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": build_user_prompt(api_spec)}
            ],
            response_format=SplunkTAConfig,
            temperature=0.2
        )
        return response.choices[0].message.parsed
    except Exception as e:
        print(f"❌ Error: {e}")
        raise
