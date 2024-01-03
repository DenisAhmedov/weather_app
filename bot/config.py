import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
API_ADDRESS = os.getenv('API_ADDRESS')
API_PORT = os.getenv('API_PORT')
