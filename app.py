import dotenv
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv(api_key)
email_addr = os.getenv(email_addr)
password = os.getenv(password)