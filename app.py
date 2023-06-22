import os
from dotenv import load_dotenv

load_dotenv()

# Setup API credentials - using env variables locally
pub_key = os.getenv('PUB-API-KEY')
pri_key = os.getenv('PRI-API-KEY')
