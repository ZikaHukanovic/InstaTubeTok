import discord
import requests

from TikTokModule import TikTokModule
from YouTubeModule import YouTubeModule
from InstagramModule import InstagramModule


class DiscordBot(discord.Client):

    def __init__(self):
        super().__init__()

        self.tiktok_module = TikTokModule()
        self.youtube_module = YouTubeModule()
        self.instagram_module = InstagramModule()

    async def on_ready(self):
        print("Bot ready!")

    async def on_message(self, message):
        if message.content.startswith("!follow"):
            username = message.content.split(" ")[1]
            platform = "TikTok"
            await self.handle_follow_command(message, username, platform)
        elif message.content.startswith("!like"):
            video_id = message.content.split(" ")[1]
            platform = "TikTok" if video_id.startswith("69420") else "YouTube"
            await self.handle_like_command(message, video_id, platform)
        elif message.content.startswith("!view"):
            video_id = message.content.split(" ")[1]
            platform = "TikTok"
            await self.handle_view_command(message, video_id, platform)

    async def handle_follow_command(self, message, username, platform):
        if platform == "TikTok":
            await self.tiktok_module.follow_user(username)
        elif platform == "YouTube":
            await self.youtube_module.subscribe_to_channel(username)
        elif platform == "Instagram":
            await self.instagram_module.follow_user(username)

    async def handle_like_command(self, message, video_id, platform):
        if platform == "TikTok":
            await self.tiktok_module.like_video(video_id)
        elif platform == "YouTube":
            await self.youtube_module.like_video(video_id)
        elif platform == "Instagram":
            await self.instagram_module.like_post(video_id)

    async def handle_view_command(self, message, video_id, platform):
        if platform == "TikTok":
            await self.tiktok_module.view_video(video_id)
        elif platform == "YouTube":
            await self.youtube_module.watch_video(video_id)
        elif platform == "Instagram":
            await self.instagram_module.view_post(video_id)


bot = DiscordBot()
bot.run()
