# Placeholder for any future config needs
import os
import json

URL = "https://www.hudl.com/login"

SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]

# Credentials are loaded from a JSON config file for local development
CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), "credentials.json")
HUDL_USERNAME = None
HUDL_PASSWORD = None
if os.path.exists(CREDENTIALS_PATH):
    with open(CREDENTIALS_PATH, "r") as f:
        creds = json.load(f)
        HUDL_USERNAME = creds.get("HUDL_USERNAME")
        HUDL_PASSWORD = creds.get("HUDL_PASSWORD")
