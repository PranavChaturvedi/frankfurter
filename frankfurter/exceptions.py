REASON_NOT_FOUND = "Reason Not Found"


class FrankfurterCallFailedException(Exception):
    def __init__(self, response: dict = None, *args: object) -> None:
        super().__init__(*args)
        self.reason = response.get("reason", REASON_NOT_FOUND)
        raise Exception(
            f'Frankfurter API call has failed. \nStatusCode : {response.get("statusCode")} \nReason : {self.reason}'
        )


class UnknownCurrencyException(Exception):
    pass
