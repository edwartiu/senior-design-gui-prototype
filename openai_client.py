from openai import OpenAI
import os

""" OpenAI Client object that will facilitate communication between 
user and OpenAI API
"""
class OpenAIClient:
    def __init__(self):
        """
        Initializes an instance of OpenAIClient
        """
        self.set_api_key()
        self.client = OpenAI()


    def set_api_key(self):
        """
        Retrieves OpenAI key stored in file 'openai_apikey.txt' and sets an environment variable for the API key
        """
        with open("./openai_apikey.txt", "r") as f_obj:
            api_key = f_obj.read().strip()

        os.environ["OPENAI_API_KEY"] = api_key


    def upload_text_prompt(self, prompt: str) -> str:
        """
        Makes an API call to OpenAI where the given prompt is processed
        """
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content
    

    def upload_image(self, ) -> str:
        """
        Makes an API call to OpenAI where image is processed to determine objects 
        within a camera image
        """
        return None
    
