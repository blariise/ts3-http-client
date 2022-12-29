"""
Class with all commands
"""
from typing import Optional
from httpx import Response

class Commands():
    """
    Collection of commands to operate web query
    """
    def apikey_add(
        self,
        scope: Optional[str] = None,
        lifetime: Optional[int] = None,
        cldbid: Optional[int] = None,
    ) -> Response:

        params = {
            'scope': scope,
            'lifetime': lifetime,
            'cldbid': cldbid
        }
        return self.query('apikeyadd', params)

    def ban_add(
        self,
        ip: Optional[str] = None,
        name: Optional[str] = None,
        uid: Optional[int] = None,
        mytsid: Optional[int] = None,
        time: Optional[int] = None,
        banreason: Optional[str] = None,
        lastnickname: Optional[str] = None
    ) -> Response:

        params = {
            'ip': ip,
            'name': name,
            'uid': uid,
            'mytsid': mytsid,
            'time': time,
            'banreason': banreason,
            'lastnickname': lastnickname
        }
        return self.query('banadd', params)

    def ban_client(
        self,
        continueonerror: Optional[bool] = None,
        clid: Optional[int] = None,
        time: Optional[int] = None,
        banreason: Optional[int] = None
    ) -> Response:
        params = {
            'clid': clid,
            'time': time,
            'banreason': banreason
        }
        if continueonerror is True:
            params['-continueonerror'] = ''

        return self.query('banclient', params)

    def whoami(self) -> Response:
        return self.query('whoami')
        