class ErrorBot(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'CustomError: {self.message} '
        else:
            return 'CustomError has been raised'


# Call of MyCustomError

raise ErrorBot('Oh, I have a bad feeling about this')