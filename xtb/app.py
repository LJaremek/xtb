from datetime import datetime
import websocket
import json

from .constants import PERIOD


class XTB:
    def __init__(
            self,
            user_id: str,
            password: str,
            version: str = "demo"
            ) -> None:

        self.version = version
        url = f"wss://ws.xtb.com/{version}"
        self.ws = websocket.create_connection(url)
        self.user_id = user_id
        self.__password = password

    def _parse_date_to_unix(self, date_str: str) -> int:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")

        unix_timestamp = int(date_obj.timestamp()) * 1000

        return unix_timestamp

    def send_message(self, message: dict) -> dict:
        self.ws.send(json.dumps(message))
        return json.loads(self.ws.recv())

    def login(self) -> dict:
        message = {
            "command": "login",
            "arguments": {
                "userId": self.user_id,
                "password": self.__password
            }
        }
        return self.send_message(message)

    def get_chart_range_request(
            self,
            start: int,
            end: int,
            symbol: str,
            period: int | str = "W1",
            ticks: int = 0
            ) -> dict:

        if end in ("today", "now"):
            end = datetime.now().strftime("%Y-%m-%d")

        if type(period) is str:
            period = PERIOD[period]

        start = self._parse_date_to_unix(start)
        end = self._parse_date_to_unix(end)

        message = {
            "command": "getChartRangeRequest",
            "arguments": {
                "info": {
                    "period": period,
                    "start": start,
                    "end": end,
                    "symbol": symbol,
                    "ticks": ticks
                }
            }
        }
        return self.send_message(message)

    def get_news(self, start: int, end: int) -> dict:
        if end in ("today", "now"):
            end = datetime.now().strftime("%Y-%m-%d")

        start = self._parse_date_to_unix(start)
        end = self._parse_date_to_unix(end)

        message = {
            "command": "getNews",
            "arguments": {
                "start": start,
                "end": end
            }
        }

        return self.send_message(message)
