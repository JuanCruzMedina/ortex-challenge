class UnsupportedExtensionError(Exception):

    def __init__(self, extension: str, message: str) -> None:
        self.extension = extension
        self.message = message
        super().__init__(message)


class InvalidMonthNumberError(Exception):

    def __init__(self, number: int, message: str) -> None:
        self.number = number
        self.message = message
        super().__init__(message)


class NoExchangesAvailableError(Exception):

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)
