from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler
from telegram.ext._utils.types import FilterDataDict
from telegram.ext.filters import UpdateFilter
from app.secrets import ADMIN_ID
from typing import Any


class __FromAdminFilter(UpdateFilter):
    def check_update(self, update: Update) -> bool | dict[str, list[Any]] | None:
        if update.effective_user.id == ADMIN_ID:
            return True


FROMADMIN = __FromAdminFilter("FromAdmin")


class Bot:
    def __init__(self, token: str, proxy: str = None, use_proxy: bool = True):
        """Create an instance of python-telegram-bot `Application` using the application builder

        Args:
            token (str): Telegram bot token from `@BotFather`
            proxy (str, optional): url for proxy eg:`http://example.com` or `socks5h://example.com`. Defaults to None.
            use_proxy (bool, optional): this parameter is used for more control on proxy usage in different environments. Defaults to True.
        """
        if proxy is not None and use_proxy:
            self.app = ApplicationBuilder().token(token).proxy(proxy).build()
        else:
            self.app = ApplicationBuilder().token(token).build()

    def command(self, func=None, *, command: str = None):
        if func is None:

            def wrapper(func):
                self.app.add_handler(CommandHandler(command, func))
                return func

            return wrapper
        self.app.add_handler(CommandHandler(func.__name__, func))
        return func

    def admin_command(self, func=None, *, command: str = None):
        if func is None:

            def wrapper(func):
                self.app.add_handler(CommandHandler(command, func, filters=[FROMADMIN]))
                return func

            return wrapper
        self.app.add_handler(CommandHandler(func.__name__, func, filters=[FROMADMIN]))
        return func

    def handler(self, handler, **kwargs):
        def wrapper(func):
            self.app.add_handler(handler(callback=func, **kwargs))
            return func

        return wrapper
