# InstagramModule.py

import requests
import json


class InstagramModule:

    def __init__(self):
        self.api_key = "YOUR_API_KEY"
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"

    async def follow_user(self, username):
        url = f"https://graph.instagram.com/v1/users/{username}/follow"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "User-Agent": self.user_agent,
        }

        response = requests.post(url, headers=headers)

        if response.status_code == 200:
            return True
        else:
            return False

    async def like_post(self, post_id):
        url = f"https://graph.instagram.com/v1/media/{post_id}/likes"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "User-Agent": self.user_agent,
        }

        response = requests.post(url, headers=headers)

        if response.status_code == 200:
            return True
        else:
            return False

    async def comment_on_post(self, post_id, message):
        url = f"https://graph.instagram.com/v1/media/{post_id}/comments"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "User-Agent": self.user_agent,
            "Content-Type": "application/json",
        }

        payload = {
            "text": message,
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            return True
        else:
            return False

