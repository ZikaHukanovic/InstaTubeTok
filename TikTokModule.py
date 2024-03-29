# TikTokModule.py

import requests


class TikTokModule:

    def __init__(self):
        self.api_key = "YOUR_API_KEY"

    async def follow_user(self, username):
        url = f"https://api.tiktok.com/v1/users/{username}/follow"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
        }

        response = requests.post(url, headers=headers)

        if response.status_code == 200:
            return True
        else:
            return False

    async def like_video(self, video_id):
        url = f"https://api.tiktok.com/v1/videos/{video_id}/like"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
        }

        response = requests.post(url, headers=headers)

        if response.status_code == 200:
            return True
        else:
            return False

    async def view_video(self, video_id):
        url = f"https://api.tiktok.com/v1/videos/{video_id}/play"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
        }

        response = requests.post(url, headers=headers)

        if response.status_code == 200:
            return True
        else:
            return False
