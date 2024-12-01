# MTMwNzY2OTQ0OTE3MTUzODA0MQ.GjgMQD.UlpsZR_bI_PZ-Xzn2x7LTgmFt_hUlCi6SlNGCk

import discord
from discord.ext import commands
import asyncio


async def run_bot(link, channel_id='1306211290196217867',
                  token='MTMwNzY2OTQ0OTE3MTUzODA0MQ.GjgMQD.UlpsZR_bI_PZ-Xzn2x7LTgmFt_hUlCi6SlNGCk'):
    # bot = commands.Bot(command_prefix='!', help_command=None, intents=discord.Intents.all())
    try:
        bot = commands.Bot(command_prefix='!', help_command=None, intents=discord.Intents.all())

        # channel = bot.get_channel(int(channel_id))
        # if channel is None:
        #     print(f"Канал с ID {channel_id} не найден.")
        #     return

        @bot.event
        async def on_ready():
            print(f'Бот запущен {bot.user}')
            channel = bot.get_channel(int(channel_id))
            if channel is None:
                print(f"Канал с ID {channel_id} не найден.")
                await bot.close()
                return

            await asyncio.sleep(2)

            try:
                await channel.send(f'!play {link}')
            except discord.Forbidden:
                print("Бот не имеет прав отправлять сообщения в указанный канал.")
            except Exception as e:
                print(f"Произошла ошибка при отправке сообщения: {e}")
            finally:
                await bot.close()

        try:
            await bot.start(token)

        except Exception as e:
            print(f"Произошла ошибка: {e}")
        finally:
            print("Бот остановлен.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


async def send_pause_command(channel_id,
                             token='MTMwNzY2OTQ0OTE3MTUzODA0MQ.GjgMQD.UlpsZR_bI_PZ-Xzn2x7LTgmFt_hUlCi6SlNGCk'):
    # bot = commands.Bot(command_prefix='!', help_command=None, intents=discord.Intents.all())
    try:
        bot = commands.Bot(command_prefix='!', help_command=None, intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            print(f'Бот запущен {bot.user}')
            channel = bot.get_channel(int(channel_id))
            if channel is None:
                print(f"Канал с ID {channel_id} не найден.")
                await bot.close()
                return

            await asyncio.sleep(2)

            try:
                await channel.send(f'!pause')
            except discord.Forbidden:
                print("Бот не имеет прав отправлять сообщения в указанный канал.")
            except Exception as e:
                print(f"Произошла ошибка при отправке сообщения: {e}")
            finally:
                await bot.close()

        try:
            await bot.start(token)

        except Exception as e:
            print(f"Произошла ошибка: {e}")
        finally:
            print("Бот остановлен.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


async def send_unpause_command(channel_id,
                               token='MTMwNzY2OTQ0OTE3MTUzODA0MQ.GjgMQD.UlpsZR_bI_PZ-Xzn2x7LTgmFt_hUlCi6SlNGCk'):
    # bot = commands.Bot(command_prefix='!', help_command=None, intents=discord.Intents.all())
    try:
        bot = commands.Bot(command_prefix='!', help_command=None, intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            print(f'Бот запущен {bot.user}')
            channel = bot.get_channel(int(channel_id))
            if channel is None:
                print(f"Канал с ID {channel_id} не найден.")
                await bot.close()
                return

            await asyncio.sleep(2)

            try:
                await channel.send(f'!resume')
            except discord.Forbidden:
                print("Бот не имеет прав отправлять сообщения в указанный канал.")
            except Exception as e:
                print(f"Произошла ошибка при отправке сообщения: {e}")
            finally:
                await bot.close()

        try:
            await bot.start(token)

        except Exception as e:
            print(f"Произошла ошибка: {e}")
        finally:
            print("Бот остановлен.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
