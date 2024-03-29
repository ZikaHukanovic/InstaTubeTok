# YouTubeModule.py

import requests


class YouTubeModule:

    def __init__(self):
        self.api_key = "YOUR_API_KEY"

    async def subscribe_to_channel(self, channel_id):
        url = f"https://www.googleapis.com/youtube/v3/channels/{channel_id}/subscriptions?part=snippet"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "snippet": {
                "resourceId": {
                    "kind": "youtube#channel",
                    "channelId": channel_id,
                },
            },
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            return True
        else:
            return False

    async def like_video(self, video_id):
        url = f"https://www.googleapis.com/youtube/v3/videos/{video_id}/likes?part=snippet"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "snippet": {
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id,
                },
            },
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            return True
        else:
            return False

    async def comment_on_video(self, video_id, message):
        url = f"https://www.googleapis.com/youtube/v3/videos/{video_id}/comments?part=snippet"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "snippet": {
                "authorDetails": {
                    "channelId": "YOUR_CHANNEL_ID",
                },
                "textOriginal": message,
            },
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            return True
        else:
            return False
