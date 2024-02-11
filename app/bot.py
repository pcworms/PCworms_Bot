from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler


class Bot:
    def __init__(self, token):
        self.app = ApplicationBuilder().token(token).build()

    def command(self, func=None, command: str = None):
        if func is None:

            def wrapper(func):
                self.app.add_handler(CommandHandler(command, func))
                return func

            return wrapper
        self.app.add_handler(CommandHandler(func.__name__, func))
        return func

    def handler(self, handler, **kwargs):
        def wrapper(func):
            self.app.add_handler(handler(callback=func, **kwargs))
            return func

        return wrapper
