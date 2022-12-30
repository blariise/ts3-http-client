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

    def apikey_del(
        self,
        id: Optional[int] = None
    ) -> Response:

        params = {
            'id': id
        }
        return self.query('apikeydel', params)

    def apikey_list(
        self,
        cldbid: Optional[int] = None,
        start: Optional[int] = None,
        duration: Optional[int] = None,
        count: Optional[bool] = None
    ) -> Response:

        params = {
            'cldbid': cldbid,
            'start': start,
            'duration': duration,
        }
        if count is True:
            params['-count'] = ''
        return self.query('apikeylist', params)

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
        clid: Optional[int] = None,
        time: Optional[int] = None,
        banreason: Optional[int] = None,
        continueonerror: Optional[bool] = None
    ) -> Response:

        params = {
            'clid': clid,
            'time': time,
            'banreason': banreason
        }
        if continueonerror is True:
            params['-continueonerror'] = ''
        return self.query('banclient', params)

    def ban_del(
        self,
        banid: Optional[int] = None
    ) -> Response:

        params = {
            'banid': banid
        }
        return self.query('bandel', params)

    def ban_del_all(
        self
    ) -> Response:
        return self.query('bandelall')

    def ban_list(
        self,
        start: Optional[int] = None,
        duration: Optional[int] = None,
        count: Optional[bool] = None
    ) -> Response:

        params = {
            'start': start,
            'duration': duration,
        }
        if count is True:
            params['count'] = ''
        return self.query('banlist', params)

    def binding_list(
        self,
        subsystem: Optional[str] = None
    ) -> Response:

        params = {
            'subsystem': subsystem 
        }
        return self.query('bindinglist', params)

    def ch_add_perm(
        self,
        cid: Optional[int] = None,
        permid: Optional[int] = None,
        permsid: Optional[int] = None,
        permvalue: Optional[int] = None,
        continueonerror: Optional[bool] = None
    ) -> Response:

        params = {
            'cid': cid,
            'permid': permid,
            'permsid': permsid,
            'permvalue': permvalue
        }
        if continueonerror is True:
            params['-continueonerror'] = ''
        return self.query('channeladdperm', params)

    def ch_client_add_perm(
        self,
        cid: Optional[int] = None,
        cldbid: Optional[int] = None,
        permid: Optional[int] = None,
        permsid: Optional[int] = None,
        permvalue: Optional[int] = None,
        continueonerror: Optional[bool] = None
    ) -> Response:

        params = {
            'cid': cid,
            'cldbid': cldbid,
            'permid': permid,
            'permsid': permsid,
            'permvalue': permvalue
        }
        if continueonerror is True:
            params['-continueonerror'] = ''
        return self.query('channelclientaddperm', params)

    def ch_client_del_perm(
        self,
        cid: Optional[int] = None,
        cldbid: Optional[int] = None,
        permid: Optional[int] = None,
        permsid: Optional[int] = None
    ) -> Response:

        params = {
            'cid': cid,
            'cldbid': cldbid,
            'permid': permid,
            'permsid': permsid,
        }
        return self.query('channelclientpermlist', params)

    def ch_client_perm_list(
        self,
        cid: Optional[int] = None,
        cldbid: Optional[int] = None,
        permsid: Optional[bool] = None
    ) -> Response:

        params = {
            'cid': cid,
            'cldbid': cldbid,
            'permsid': permsid
        }
        if permsid is True:
            params['-permsid'] = ''
        return self.query('channelclientaddperm', params)

    def whoami(self) -> Response:
        return self.query('whoami')
        