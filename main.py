"""
1) createing a telegram bot using botfather
2) getting telegram bot token
3) getting chat id 
4) sending message using python
"""

TOKEN = 'TOKEN'
CHAT_ID = 'CHAT_ID'
import requests
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())

message = 'Hello For Telegram Bot'
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"

r = requests.get(url)
print(r.json)