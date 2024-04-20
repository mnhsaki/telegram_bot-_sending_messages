# Title: Telegram Bot - Sending Messages (Secure Version)

## Description:

This Python script demonstrates how to send a basic message to a Telegram chat using the Telegram Bot API. However, it's important to **never commit your Telegram Bot Token or Chat ID to a public repository due to security risks**.

## Prerequisites:

- A Telegram account
- A Telegram bot created using BotFather ([invalid URL removed])
- **chat id**
  
## Installation:

1. Install the **requests** library using pip:

```
Bash

pip install requests
```

## Configuration (Secure):

1. Obtain your Telegram Bot Token: Create a bot using BotFather and retrieve its token. Do not commit this token to your public repository. You can store it securely using environment variables or a separate configuration file.
2. Obtain the Chat ID: Start a chat with your bot and send a message. You can then use the Telegram API Explorer ([invalid URL removed]) to get the Chat ID from the response. Do not commit this ID to your public repository either. Store it securely following the same approach as the Bot Token.
   
## Code Structure:

```
Python
import requests

# Replace with your securely stored Telegram Bot Token (e.g., from environment variables)
TOKEN = None

# Replace with the Chat ID of the recipient (e.g., from a configuration file)
CHAT_ID = None

message = 'Hello From Telegram Bot!'

# Construct the URL securely using f-strings and placeholder variables
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"

try:
  # Send the message
  response = requests.get(url)
  response.raise_for_status()  # Raise an exception for non-200 status codes
  print("Message sent successfully!")
except requests.exceptions.RequestException as e:
  print(f"An error occurred while sending the message: {e}")
```


## Explanation:

- The script imports the **requests** library for making HTTP requests to the Telegram API.
- Placeholder Variables: The **TOKEN** and **CHAT_ID** are replaced with placeholder variables to emphasize the importance of not committing them to public code.
- Secure URL Construction: The API URL is constructed using f-strings and placeholder variables, promoting security and readability.
- Error Handling: The code includes **try-except** blocks to handle potential errors during the HTTP request and raise an exception for non-200 status codes. This helps in debugging and identifying issues.
  
## Usage (Example):

1. Set environment variables or a secure configuration file for **TOKEN** and **CHAT_ID**.
2. Run the script using **python your_script.py**.

## Security Considerations:

- Never commit sensitive credentials to public repositories. Store them securely using environment variables or a dedicated configuration file.
- Avoid hardcoding these values in your code. This makes your script less portable and introduces security risks.

## Additional Notes:

- This example sends a simple message. The Telegram Bot API offers more advanced features like sending photos, documents, and location data.


**Remember**: This code is for educational purposes only. Be responsible and use Telegram bots ethically.