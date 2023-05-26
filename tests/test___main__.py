import asyncio
import datetime
import unittest
from unittest.mock import AsyncMock, patch
from discord.ext import commands


class TestBot(unittest.TestCase):

    def setUp(self) -> None:
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def tearDown(self) -> None:
        self.loop.close()
        asyncio.set_event_loop(None)

    @patch('discord.Message')
    @patch('discord.ext.commands.Context')
    def test_poll(self, mock_ctx, mock_msg):
        # Mocking the necessary discord objects
        mock_msg.add_reaction = AsyncMock()
        mock_ctx.send = AsyncMock(return_value=mock_msg)

        from helpy_discord_bot.__main__ import _poll

        self.loop.run_until_complete(_poll(mock_ctx, "poll_name", "option1", "option2"))

        # Ensure the poll message is correct
        msg = mock_ctx.send.call_args[0][0]
        self.assertEqual(msg, 'New poll\n**poll_name**\n🇦 option1\n🇧 option2')

        # Ensure the reactions are added correctly
        self.assertEqual(mock_msg.add_reaction.call_count, 2)
        self.assertEqual(mock_msg.add_reaction.call_args_list[0][0][0], chr(127462))
        self.assertEqual(mock_msg.add_reaction.call_args_list[1][0][0], chr(127462 + 1))

    @patch('discord.Message')
    @patch('discord.ext.commands.Context')
    def test_hello(self, mock_ctx, mock_msg):
        # Mocking the necessary discord objects
        mock_ctx.author.name = "test_user"
        mock_ctx.send = AsyncMock(return_value=mock_msg)

        from helpy_discord_bot.__main__ import _hello

        self.loop.run_until_complete(_hello(mock_ctx))

        # Ensure the hello message is correct
        msg = mock_ctx.send.call_args[0][0]
        self.assertEqual(msg, f"Hello {mock_ctx.author.name}!")

    @patch('discord.Message')
    @patch('discord.ext.commands.Context')
    def test_current_time(self, mock_ctx, mock_msg):
        # Mocking the necessary discord objects
        mock_ctx.send = AsyncMock(return_value=mock_msg)

        from helpy_discord_bot.__main__ import _current_time

        self.loop.run_until_complete(_current_time(mock_ctx))

        # Ensure the current time message is correct
        msg = mock_ctx.send.call_args[0][0]
        now = datetime.datetime.now()
        self.assertEqual(msg, f"The current time is {now.hour:02d}:{now.minute:02d}")

    @patch('discord.Message')
    @patch('discord.ext.commands.Context')
    def test_help(self, mock_ctx, mock_msg):
        # Mocking the necessary discord objects
        mock_ctx.send = AsyncMock(return_value=mock_msg)

        from helpy_discord_bot.__main__ import _help

        self.loop.run_until_complete(_help(mock_ctx))

        # Ensure the help message is correct
        msg = mock_ctx.send.call_args[0][0]
        print(msg)

if __name__ == '__main__':
    unittest.main()