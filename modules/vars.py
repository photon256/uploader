import os

API_ID    = os.environ.get("API_ID", "16253557")
API_HASH  = os.environ.get("API_HASH", "81171c25e4cb9062cb10da8b7730432a")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7727539440:AAE3rV1XiLbBR9MALXIDlqMO6xDFsxLJtLE") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
