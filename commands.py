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

    def whoami(self) -> Response:
        return self.query('whoami')
        