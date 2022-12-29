"""
.
"""

from httpx import Response, post
from commands import Commands
from typing import Optional

class Query(Commands):
    """
    Class that send query and verify post request
    """

    def __init__(self) -> None:
        return None

    def remove_none(self, dictionary):
        new_dict = {
            key: value for key, value in dictionary.items() if value is not None
        }
        return new_dict

    def query(
        self,
        command: Optional[str] = None,
        params: Optional[dict] = None,
    ) -> Response:
        if params is not None:
            params = self.remove_none(params)
        else:
            params = {}
        params['api-key'] = self.api_key
        r = post(self.get_url() + command, params=params)
        status = r.json()['status']
        if status != 0:
            print(status['message'])
        return r
        