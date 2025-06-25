import asyncio
from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot

class Command(BaseCommand):
    help = 'Send a test message using your Telegram bot'

    def handle(self, *args, **kwargs):
        chat_id = input("Enter your Telegram chat ID: ")
        message = "Hello from your Django Telegram bot! 🚀"

        # Run async method in sync context
        asyncio.run(self.send_message(chat_id, message))

    async def send_message(self, chat_id, message):
        bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
        await bot.send_message(chat_id=chat_id, text=message)
        print(f"Message sent to {chat_id}")
