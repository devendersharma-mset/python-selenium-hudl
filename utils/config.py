# Placeholder for any future config needs
import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

URL = "https://www.hudl.com/login"

SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]

# Credentials are loaded from .env file
HUDL_USERNAME = os.getenv("HUDL_USERNAME")
HUDL_PASSWORD = os.getenv("HUDL_PASSWORD")
