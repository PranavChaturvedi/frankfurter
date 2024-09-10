from .logger import Logger
from .utils import BASE_URL, BASE_HEADERS
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError
from http import HTTPMethod
from .exceptions import FrankfurterCallFailedException, UnknownCurrencyException
import json
from functools import cache


class FrankfurterEngine:
    def __init__(self, quiet_mode: bool = True) -> None:
        self.quiet_mode = quiet_mode
        if not quiet_mode:
            Logger.info("Currency Engine Initiallized")
        self.__base_url = BASE_URL
        self.__base_headers = BASE_HEADERS

    def __api_call(
        self, query_params: dict = {}, path_params: str = [], extra_headers: dict = {}
    ) -> dict:
        """Handles the API request core logic."""
        params_str = urlencode({k: v for k, v in query_params.items() if v})
        path_params = "/".join(path_params)
        request = Request(
            url=f"https://{self.__base_url}/{path_params}?{params_str}",
            method=HTTPMethod.GET,
            headers={**self.__base_headers, **extra_headers},
        )
        try:
            with urlopen(request) as response:
                if not self.quiet_mode:
                    Logger.info("Found the Forex data successfully")
                response: dict = json.loads(response.read().decode())
                return response
        except HTTPError as e:
            raise FrankfurterCallFailedException(
                {"statusCode": e.code, "reason": e.msg}
            )

    def _check_valid_currency(self, currency):
        """Validates if the currency code exists."""
        if currency not in self.fetch_currencies().keys():
            raise UnknownCurrencyException(f"Unknown Currency : {currency}")

    def fetch_latest_data(self, base: str = None, to: str = None) -> dict:
        """
        Fetches the latest forex data provided by the European Central Bank.

        Parameters:
            base (str): The base currency to convert from (optional, default: EUR).
            to (str): The target currency to convert to (optional).

        Returns:
            dict: Latest forex data for the provided base and target currencies.
        """
        if base:
            self._check_valid_currency(base)
        if to:
            self._check_valid_currency(to)
        query_params = {"from": base, "to": to}
        return self.__api_call(query_params, path_params=["latest"])

    def fetch_time_series_data(
        self,
        base: str = None,
        to: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> dict:
        """
        Fetches forex data for a specified time range.

        Parameters:
            base (str): The base currency to convert from (optional, default: EUR).
            to (str): The target currency to convert to (optional).
            start_date (str): The start date in YYYY-MM-DD format (required).
            end_date (str): The end date in YYYY-MM-DD format (optional). If not given, the data from start_date to the present day is returned.

        Returns:
            dict: Forex data for the given time range.
        """
        if base:
            self._check_valid_currency(base)
        if to:
            self._check_valid_currency(to)
        query_params = {"from": base, "to": to}
        if not start_date:
            return self.fetch_latest_data(base, to)
        path_params = f"{start_date}..{end_date or ""}"
        return self.__api_call(query_params=query_params, path_params=[path_params])

    def fetch_data_for_date(self, date: str, base: str = None, to: str = None) -> dict:
        """
        Fetches forex data for a specific date.

        Parameters:
            date (str): The specific date in YYYY-MM-DD format.
            base (str): The base currency to convert from (optional, default: EUR).
            to (str): The target currency to convert to (optional).

        Returns:
            dict: Forex data for the specified date.
        """
        if base:
            self._check_valid_currency(base)
        if to:
            self._check_valid_currency(to)
        query_params = {"from": base, "to": to}
        return self.__api_call(query_params=query_params, path_params=[date])

    @cache
    def fetch_currencies(self):
        """
        Fetches the list of supported currencies.

        Returns:
            dict: A dictionary of supported currencies where the keys are currency codes.
        """
        return self.__api_call(path_params=["currencies"])

    def convert_currency(self, amount: float, base: str, to: str) -> float:
        """
        Converts a specified amount from one currency to another using the latest exchange rate.

        Parameters:
            amount (float): The amount to convert.
            base (str): The source currency.
            to (str): The target currency.

        Returns:
            float: The converted amount based on the latest exchange rate.
        """
        self._check_valid_currency(base)
        self._check_valid_currency(to)

        # Fetch the latest exchange rate data
        rates = self.fetch_latest_data(base=base, to=to)

        # Get the exchange rate from the 'rates' field
        exchange_rate = rates["rates"].get(to)

        if exchange_rate:
            return amount * exchange_rate
        else:
            raise FrankfurterCallFailedException(
                f"No exchange rate found for {base} to {to}."
            )
