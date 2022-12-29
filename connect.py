"""
.
"""
from query import Query
from typing import Optional

class Connect(Query):
    """
    Class that connect and send queries to Teamspeak 3 server.
    """

    def __init__(
        self,
        url: Optional[str] = None,
        port: Optional[int] = None,
        api_key: Optional[str] = None,
        server_id: Optional[int] = 1,
        protocol: Optional[str] ='http'
    ) -> None:
        self.url = url
        self.port = port
        self.api_key = api_key
        self.server_id = server_id
        self.protocol = protocol

    def get_url(self):
        url = f'{self.protocol}://{self.url}:{self.port}/{self.server_id}/'
        return url
        