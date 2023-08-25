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
profile = os.getenv('PROFILE')

# Connection config
klaviyo = KlaviyoAPI(pri_key, max_delay=60, max_retries=3, test_host=None)

# Hello world to print basic metrics, no filtering
Metrics = klaviyo.Metrics.get_metrics()

# Filtering Example on profiles between two timestamps 
# Filter_Profiles = klaviyo.Profiles.get_profiles(
#     filter='less-than(updated,2023-06-29T00:00:00Z),greater-than(updated,2023-04-01T00:00:00Z)'
#     )

# Get a single profile
Single_Profile = klaviyo.Profiles.get_profile(profile)
print(Single_Profile)

# Dump to JSON to get ready to be POSTed
json_data = json.dumps(Single_Profile)

# Post payload from Klaviyo to a webhook using webhook.site
response = requests.post(webhook, data = json_data)

# Isolate a single value - reuse original python dictionary before we pushed to json type
type_value = Metrics['data'][0]['type']

# Get multiple values, make a cleaner object 
all_metric_types = [item['attributes']['name'] for item in Metrics['data']]

# Format to JSON again, post again to Webhook.site
json_data_2 = json.dumps(all_metric_types)
response_2 = requests.post(webhook, data = json_data_2)