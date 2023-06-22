import os
from dotenv import load_dotenv
from klaviyo_api import KlaviyoAPI

load_dotenv()

# Setup API credentials - using env variables locally
pub_key = os.getenv('PUB-API-KEY')
pri_key = os.getenv('PRI-API-KEY')

# Connection config
klaviyo = KlaviyoAPI(pri_key, max_delay=60, max_retries=3, test_host=None)

# Hello world to print basic metrics, no filtering
print(klaviyo.Metrics.get_metrics())
