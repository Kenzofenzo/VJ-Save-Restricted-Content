import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7708732142:AAGdBAebaZZQbGxvH30hrutNedCMQ2_TdpY")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24210243"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "509031fb3790b968e489f71d591ebce5")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://tubibhjnu:CLfqaM43XrHoLguF@cluster0.ggsok.mongodb.net/?retryWrites=true&w=majority")
