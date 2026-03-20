import os
from dotenv import load_dotenv

load_dotenv()  # loads .env file

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = "U_R_LxBot"
DATABASE = "links.db"
