from .logger import Logger
from .utils import BASE_URL, BASE_HEADERS
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from http import HTTPMethod
from .exceptions import FrankfurterCallFailedException
import json
class FrankfurterEngine:

    def __init__(self, quiet_mode : bool = True) -> None:
        if not quiet_mode:
            Logger.info("Currency Engine Initiallized")
        self.__base_url = BASE_URL
        self.__base_headers = BASE_HEADERS

    def __api_call(self, extra_headers : dict = {}):
        httprequest = Request(
            url=f"https://{self.__base_url}/2024-08-15..2024-09-06",
            method=HTTPMethod.GET,
            headers={**self.__base_headers, **extra_headers}
        )
        try:
            with urlopen(httprequest) as httpresponse:
                print(httpresponse.status)
                response : dict = json.loads(httpresponse.read().decode())
        except HTTPError as e:
            raise FrankfurterCallFailedException(
                {"statusCode" : e.code, "reason" : e.msg}
            )


    