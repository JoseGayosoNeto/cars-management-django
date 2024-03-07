from os import environ
from openai import OpenAI

client = OpenAI(api_key=environ.get('OPENAI_API_KEY'))


    
def get_car_ai_bio(model, brand, year):
    message = '''
    Show me a sales description for the {year} {brand} {model} car in just 250 characters. 
    Highlight specific features of this model. Provide technical specifications for this car model.
    '''
    response = client.chat.completions.create(
        messages = [
            {
                'role': 'user',
                'content': message.format(model=model, brand=brand, year=year)
            }
        ],
        max_tokens = 1000,
        model = "gpt-3.5-turbo"
    )
    
    return response.choices[0].message.content