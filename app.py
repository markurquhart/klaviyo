import os
import requests 
import json

from dotenv import load_dotenv
from klaviyo_api import KlaviyoAPI

load_dotenv()

# Setup API credentials - using env variables locally
pub_key = os.getenv('PUB-API-KEY')
pri_key = os.getenv('PRI-API-KEY')
webhook = os.getenv('WEBHOOK-URL')

# Connection config
klaviyo = KlaviyoAPI(pri_key, max_delay=60, max_retries=3, test_host=None)

# Hello world to print basic metrics, no filtering
# Hello_World = klaviyo.Metrics.get_metrics()

# Filtering Example on profiles between two timestamps 
Filter_Profiles = klaviyo.Profiles.get_profiles(
    filter='less-than(updated,2023-06-22T00:00:00Z),greater-than(updated,2023-06-01T00:00:00Z)'
    )

# Format to JSON to ready for post
json_data = json.dumps(Filter_Profiles)


# Post payload from Klaviyo to a webhook using webhook.site
response = requests.post(webhook, data = json_data)


