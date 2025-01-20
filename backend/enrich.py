import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def enrich_organization_data(organization):
    prompt = f"""
    Analyze the following organization data:
    Name: {organization['name']}
    Location: {organization['location']}
    
    Provide insights on what is missing in their strategy or operations to grow their business.
    """
    response = openai.Completion.create(
        engine="gpt-4o-mini-2024-07-18",
        prompt=prompt,
        max_tokens=200
    )
    return response['choices'][0]['text'].strip()
