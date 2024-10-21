import requests
import os
from dotenv import load_dotenv
load_dotenv()



url = f"https://discord.com/api/v10/applications/{os.getenv('APP_ID')}/commands"

# # This is an example CHAT_INPUT or Slash Command, with a type of 1
json = {
    "name": "conversation_starter",
    "type": 1,
    "description": "Start a conversation",
    "contexts": [0,1,2],
    "integration_types": [0,1],
    "options": []
}

# For authorization, you can use either your bot token
headers = {
    "Authorization": f"Bot {os.getenv('BOT_TOKEN')}"
}

# # or a client credentials token for your app with the applications.commands.update scope
# # headers = {
# #     "Authorization": f"Bearer {os.getenv('CLIENT_TOKEN')}"
# # }

# r = requests.patch(url+"/1297011383056990218", headers=headers, json=json)

r = requests.delete(url+"/1297022181980770315", headers=headers)

print(r.json())