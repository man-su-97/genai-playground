from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Load environment variables from .env file

client = OpenAI()
