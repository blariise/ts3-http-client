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

    def ch_create(
        self,
        channel_name: Optional[str] = None,
        **kwargs
    ) -> Response:

        params = {
            'channel_name': channel_name
        }
        params += kwargs
        return self.query('channelcreate', params)

    def ch_delete(
        self,
        cid: Optional[int] = None,
        force: Optional[int] = None
    ) -> Response:

        params = {
            'cid': cid,
            'force': force
        }
        return self.query('channeldelete', params)

    def ch_del_perm(
        self,
        cid: Optional[int] = None,
        permid: Optional[int] = None,
        permsid: Optional[int] = None,
    ) -> Response:

        params = {
            'cid': cid,
            'permid': permid,
            'permsid': permsid
        }
        return self.query('channeldelperm', params)

    def ch_edit(
        self,
        cid: Optional[int] = None,
        cpid: Optional[int] = None,
        channel_name: Optional[str] = None,
        channel_topic: Optional[str] = None,
        channel_description: Optional[str] = None,
        channel_password: Optional[str] = None,
        channel_codec: Optional[int] = None,
        channel_codec_quality: Optional[int] = None,
        channel_maxclients: Optional[int] = None,
        channel_maxfamilyclients: Optional[int] = None,
        channel_order: Optional[int] = None,
        channel_flag_permanent: Optional[bool] = None,
        channel_flag_semi_permanent: Optional[bool] = None,
        channel_flag_default: Optional[bool] = None,
        channel_codec_is_unencrypted: Optional[bool] = None,
        channel_flag_maxclients_unlimited: Optional[int] = None,
        channel_flag_maxfamilyclients_unlimited: Optional[bool] = None,
        channel_flag_maxfamilyclients_inherited: Optional[bool] = None,
        channel_needed_talk_power: Optional[bool] = None,
        channel_name_phonetic: Optional[str] = None,
        channel_icon_id: Optional[str] = None,
        channel_banner_gfx_url: Optional[str] = None,
        channel_banner_mode: Optional[int] = None,

    ) -> Response:

        params = {
            'cid': cid,
            'cpid': cpid,
            'channel_name': channel_name,
            'channel_topic': channel_topic,
            'channel_description': channel_description,
            'channel_password': channel_password,
            'channel_codec': channel_codec,
            'channel_codec_quality': channel_codec_quality,
            'channel_maxclients': channel_maxclients,
            'channel_maxfamilyclients': channel_maxfamilyclients,
            'channel_order': channel_order,
            'channel_flag_permanent': channel_flag_permanent,
            'channel_flag_semi_permanent': channel_flag_semi_permanent,
            'channel_flag_default': channel_flag_default,
            'channel_codec_is_unencrypted': channel_codec_is_unencrypted,
            'channel_flag_maxclients_unlimited': channel_flag_maxclients_unlimited,
            'channel_flag_maxfamilyclients_unlimited': channel_flag_maxfamilyclients_unlimited,
            'channel_flag_maxfamilyclients_inherited': channel_flag_maxfamilyclients_inherited,
            'channel_needed_talk_power': channel_needed_talk_power,
            'channel_name_phonetic': channel_name_phonetic,
            'channel_icon_id': channel_icon_id,
            'channel_banner_gfx_url': channel_banner_gfx_url,
            'channel_banner_mode': channel_banner_mode
        }
        return self.query('channeledit', params)

    def ch_find(
        self,
        pattern: Optional[str] = None
    ) -> Response:

        params = {
            'pattern': pattern
        }
        return self.query('channelfind', params)

    def ch_group_add(
        self,
        name: Optional[str] = None,
        type: Optional[int] = None
    ) -> Response:

        params = {
            'name': name,
            'type': type
        }
        return self.query('channelgroupadd', params)

    def ch_group_add_perm(
        self,
        cgid: Optional[int] = None,
        permid: Optional[int] = None,
        permsid: Optional[int] = None,
        permvalue: Optional[int] = None,
        continueonerror: Optional[bool] = None
    ) -> Response:

        params = {
            'cgid': cgid,
            'permid': permid,
            'permsid': permsid,
            'permvalue': permvalue,
        }
        if continueonerror is True:
            params['-continueonerror'] = ''
        return self.query('channelgroupaddperm', params)

    def ch_group_client_list(
        self,
        cid: Optional[int] = None,
        cldbid: Optional[int] = None,
        cgid: Optional[int] = None,
    ) -> Response:

        params = {
            'cid': cid,
            'cldbid': cldbid,
            'cgid': cgid,
        }
        return self.query('channelgroupclientlist', params)

    def ch_group_copy(
        self,
        scgid: Optional[int] = None,
        tcgid: Optional[int] = None,
        name: Optional[str] = None,
        type: Optional[int] = None,
    ) -> Response:

        params = {
            'scgid': scgid,
            'tcgid': tcgid,
            'name': name,
            'type': type,
        }
        return self.query('channelgroupcopy', params)

    def ch_group_del(
        self,
        cgid: Optional[int] = None,
        force: Optional[int] = None
    ) -> Response:

        params = {
            'cgid': cgid,
            'force': force
        }
        return self.query('channelgroupdel', params)

    def ch_group_del_perm(
        self,
        cgid: Optional[int] = None,
        permid: Optional[int] = None,
        permsid: Optional[int] = None,
        continueonerror: Optional[bool] = None
    ) -> Response:

        params = {
            'cgid': cgid,
            'permid': permid,
            'permsid': permsid
        }
        if continueonerror is True:
            params['-continueonerror'] = ''
        return self.query('channelgroupdelperm', params)

    def ch_group_list(self) -> Response:
        return self.query('channelgrouplist')

    def ch_group_perm_list(
        self,
        cgid: Optional[int] = None,
        permsid: Optional[bool] = None
    ) -> Response:

        params = {
            'cgid': cgid
        }
        if permsid is True:
            params['-permsid'] = ''
        return self.query('channelgrouppermlist', params)

    def ch_group_rename(
        self,
        cgid: Optional[int] = None,
        name: Optional[str] = None
    ) -> Response:

        params = {
            'cgid': cgid,
            'name': name
        }
        return self.query('channelgrouprename', params)

    def ch_info(
        self,
        cid: Optional[int] = None
    ) -> Response:

        params = {
            'cid': cid
        }
        return self.query('channelinfo', params)

    def ch_list(self) -> Response:
        return self.query('channellist')

    def ch_move(
        self,
        cid: Optional[int] = None,
        cpid: Optional[int] = None,
        order: Optional[int] = None
    ) -> Response:

        params = {
            'cid': cid,
            'cpid': cpid,
            'order': order
        }
        return self.query('channelmove', params)

    def ch_perm_list(
        self,
        cid: Optional[int] = None,
        permsid: Optional[bool] = None
    ) -> Response:

        params = {
            'cid': cid,
        }
        if permsid is True:
            params['-permsid'] = ''
        return self.query('channelpermlist', params)

    def client_add_server_group(
        self,
        cldbid: Optional[int] = None,
        sgid: Optional[int] = None,
        continueonerror: Optional[bool] = None
    ) -> Response:

        params = {
            'cldbid': cldbid,
            'sgid': sgid
        }
        if continueonerror is True:
            params['-continueonerror'] = ''
        return self.query('clientaddservergroup', params)

    def client_db_delete(
        self,
        cldbid: Optional[int] = None
    ) -> Response:

        params = {
            'cldbid': cldbid
        }
        return self.query('clientdbdelete', params)

    def client_db_edit(
        self,
        cldbid: Optional[int] = None,
        client_description: Optional[str] = None
    ) -> Response:

        params = {
            'cldbid': cldbid,
            'client_description': client_description
        }
        return self.query('clientdbedit', params)

    def client_db_find(
        self,
        cldbid: Optional[int] = None
    ) -> Response:

        params = {
            'cldbid': cldbid
        }
        return self.query('clientdbfind', params)

    def client_db_list(
        self,
        start: Optional[int] = None,
        duration: Optional[int] = None,
        count: Optional[bool] = None
    ) -> Response:

        params = {
            'start': start,
            'duration': duration
        }
        if count is True:
            params['-count'] = ''
        return self.query('clientdblist', params)

    def client_del_perm(
        self,
        cldbid: Optional[int] = None,
        permid: Optional[int] = None
    ) -> Response:

        params = {
            'cldbid': cldbid,
            'permid': permid
        }
        return self.query('clientdelperm', params)

    def client_del_server_group(
        self,
        cldbid: Optional[int] = None,
        sgid: Optional[int] = None,
        continueonerror: Optional[bool] = None
    ) -> Response:

        params = {
            'cldbid': cldbid,
            'sgid': sgid
        }
        if continueonerror is True:
            params['-continueonerror'] = ''
        return self.query('clientdelservergroup', params)

    def client_edit(
        self,
        clid: Optional[int] = None,
        client_nickname: Optional[str] = None,
        client_description: Optional[str] = None
    ) -> Response:

        params = {
            'clid': clid,
            'client_nickname': client_nickname,
            'client_description': client_description
        }
        return self.query('clientedit', params)

    def client_find(
        self,
        pattern: Optional[str] = None
    ) -> Response:

        params = {
            'pattern': pattern
        }
        return self.query('clientfind', params)

    def client_get_db_id_from_uid(
        self,
        cluid: Optional[int] = None
    ) -> Response:

        params = {
            'cluid': cluid
        }
        return self.query('clientgetdbidfromuid', params)

    def client_get_ids(
        self,
        cluid: Optional[int] = None
    ) -> Response:

        params = {
            'cluid': cluid
        }
        return self.query('clientgetids', params)

    def client_get_name_from_db_id(
        self,
        cldbid: Optional[int] = None
    ) -> Response:

        params = {
            'cldbid': cldbid
        }
        return self.query('clientgetnamefromdbid', params)

    def client_get_name_from_uid(
        self,
        cluid: Optional[int] = None
    ) -> Response:

        params = {
            'cluid': cluid
        }
        return self.query('clientgetnamefromuid', params)

    def client_get_uid_from_clid(
        self,
        clid: Optional[int] = None
    ) -> Response:

        params = {
            'clid': clid
        }
        return self.query('clientgetuidfromclid', params)

    def client_info(
        self,
        clid: Optional[int] = None
    ) -> Response:

        params = {
            'clid': clid
        }
        return self.query('clientinfo', params)

    def client_kick(
        self,
        clid: Optional[int] = None,
        reasonid: Optional[int] = None,
        reasonmsg: Optional[str] = None,
        continueonerror: Optional[bool] = None
    ) -> Response:

        params = {
            'clid': clid,
            'reasonid': reasonid,
            'reasonmsg': reasonmsg
        }
        if continueonerror is True:
            params['-continueonerror'] = ''
        return self.query('clientkick', params)

    def client_move(
        self,
        clid: Optional[int] = None,
        cid: Optional[int] = None,
        cpw: Optional[str] = None,
        continueonerror: Optional[bool] = None
    ) -> Response:

        params = {
            'clid': clid,
            'cid': cid,
            'cpw': cpw
        }
        if continueonerror is True:
            params['-continueonerror'] = ''
        return self.query('clientmove', params)

    def client_perm_list(
        self,
        cldbid: Optional[int] = None,
        permsid: Optional[bool] = None
    ) -> Response:

        params = {
            'cldbid': cldbid,
            'permsid': permsid
        }
        if permsid is True:
            params['-permsid'] = ''
        return self.query('clientpermlist', params)

    def client_poke(
        self,
        clid: Optional[int] = None,
        msg: Optional[str] = None
    ) -> Response:

        params = {
            'clid': clid,
            'msg': msg
        }
        return self.query('clientpoke', params)

    def client_set_server_query_login(
        self,
        client_login_name: Optional[str] = None
    ) -> Response:

        params = {
            'client_login_name': client_login_name
        }
        return self.query('clientsetserverquerylogin', params)

    def complain_add(
        self,
        tcldbid: Optional[int] = None,
        message: Optional[str] = None
    ) -> Response:

        params = {
            'tcldbid': tcldbid,
            'message': message
        }
        return self.query('complainadd', params)

    def complain_del(
        self,
        tcldbid: Optional[int] = None,
        fcldbid: Optional[int] = None
    ) -> Response:

        params = {
            'tcldbid': tcldbid,
            'fcldbid': fcldbid
        }
        return self.query('complaindel', params)

    def complain_del_all(
        self,
        tcldbid: Optional[int] = None
    ) -> Response:

        params = {
            'tcldbid': tcldbid
        }
        return self.query('complaindelall', params)

    def complain_list(
        self,
        tcldbid: Optional[int] = None
    ) -> Response:

        params = {
            'tcldbid': tcldbid,
        }
        return self.query('complainlist', params)

    def custom_delete(
        self,
        cldbid: Optional[int] = None,
        ident: Optional[int] = None
    ) -> Response:

        params = {
            'cldbid': cldbid,
            'ident': ident
        }
        return self.query('customdelete', params)

    def custom_info(
        self,
        cldbid: Optional[int] = None
    ) -> Response:

        params = {
            'cldbid': cldbid
        }
        return self.query('custominfo', params)

    def custom_search(
        self,
        ident: Optional[int] = None,
        pattern: Optional[str] = None
    ) -> Response:

        params = {
            'ident': ident,
            'pattern': pattern
        }
        return self.query('customsearch', params)

    def custom_set(
        self,
        cldbid: Optional[int] = None,
        ident: Optional[int] = None,
        value: Optional[str] = None
    ) -> Response:

        params = {
            'cldbid': cldbid,
            'ident': ident,
            'value': value
        }
        return self.query('customset', params)

    def ft_create_dir(
        self,
        cid: Optional[int] = None,
        cpw: Optional[str] = None,
        dirname: Optional[str] = None
    ) -> Response:

        params = {
            'cid': cid,
            'cpw': cpw,
            'dirname': dirname
        }
        return self.query('ftcreatedir', params)

    def ft_delete_file(
        self,
        cid: Optional[int] = None,
        cpw: Optional[str] = None,
        name: Optional[str] = None
    ) -> Response:

        params = {
            'cid': cid,
            'cpw': cpw,
            'name': name
        }
        return self.query('ftdeletefile', params)

    def ft_get_file_info(
        self,
        cid: Optional[int] = None,
        cpw: Optional[str] = None,
        name: Optional[str] = None
    ) -> Response:

        params = {
            'cid': cid,
            'cpw': cpw,
            'name': name
        }
        return self.query('ftgetfileinfo', params)

    def ft_get_file_list(
        self,
        cid: Optional[int] = None,
        cpw: Optional[str] = None,
        path: Optional[str] = None
    ) -> Response:

        params = {
            'cid': cid,
            'cpw': cpw,
            'path': path
        }
        return self.query('ftgetfilelist', params)

    def ft_init_download(
        self,
        clientftfid: Optional[int] = None,
        name: Optional[str] = None,
        cid: Optional[int] = None,
        cpw: Optional[str] = None,
        seekpos: Optional[int] = None,
        proto: Optional[int] = None
    ) -> Response:

        params = {
            'clientftfid': clientftfid,
            'name': name,
            'cid': cid,
            'cpw': cpw,
            'seekpos': seekpos,
            'proto': proto
        }
        return self.query('ftinitdownload', params)

    def ft_init_upload(
        self,
        clientftfid: Optional[int] = None,
        name: Optional[str] = None,
        cid: Optional[int] = None,
        cpw: Optional[str] = None,
        size: Optional[int] = None,
        overwrite: Optional[int] = None,
        resume: Optional[int] = None,
        proto: Optional[int] = None
    ) -> Response:

        params = {
            'clientftfid': clientftfid,
            'name': name,
            'cid': cid,
            'cpw': cpw,
            'size': size,
            'overwrite': overwrite,
            'resume': resume,
            'proto': proto
        }
        return self.query('ftinitupload', params)

    def ft_list(self) -> Response:
        return self.query('ftlist')

    def ft_rename_file(
        self,
        cid: Optional[int] = None,
        cpw: Optional[str] = None,
        tcid: Optional[int] = None,
        tcpw: Optional[str] = None,
        oldname: Optional[str] = None,
        newname: Optional[str] = None
    ) -> Response:

        params = {
            'cid': cid,
            'cpw': cpw,
            'tcid': tcid,
            'tcpw': tcpw,
            'oldname': oldname,
            'newname': newname
        }
        return self.query('ftrenamefile', params)

    def ft_stop(
        self,
        serverftfid: Optional[int] = None,
        delete: Optional[int] = None
    ) -> Response:

        params = {
            'serverftfid': serverftfid,
            'delete': delete
        }
        return self.query('ftstop', params)

    def gm(
        self,
        msg: Optional[str] = None
    ) -> Response:

        params = {
            'msg': msg
        }
        return self.query('gm', params)

    def host_info(self) -> Response:
        return self.query('hostinfo')

    def instance_edit(
        self,
        **kwargs
    ) -> Response:

        params = {}
        params += kwargs
        return self.query('instanceedit', params)        
    
    def instance_info(self) -> Response:
        return self.query('instanceinfo')

    def log_add(
        self,
        loglevel: Optional[int] = None,
        logmsg: Optional[str] = None
    ) -> Response:

        params = {
            'loglevel': loglevel,
            'logmsg': logmsg
        }
        return self.query('logadd', params)

    def login(
        self,
        client_login_name: Optional[str] = None,
        client_login_password: Optional[str] = None
    ) -> Response:

        params = {
            'client_login_name': client_login_name,
            'client_login_password': client_login_password
        }
        return self.query('login', params)

    def logout(self) -> Response:
        return self.query('logout')

    def log_view(
        self,
        lines: Optional[int] = None,
        reverse: Optional[int] = None,
        instance: Optional[int] = None,
        begin_pos: Optional[int] = None
    ) -> Response:

        params = {
            'lines': lines,
            'reverse': reverse,
            'instance': instance,
            'begin_pos': begin_pos
        }
        return self.query('logview', params)

    def message_add(
        self,
        cluid: Optional[int] = None,
        subject: Optional[str] = None,
        message: Optional[str] = None
    ) -> Response:

        params = {
            'cluid': cluid,
            'subject': subject,
            'message': message
        }
        return self.query('messageadd', params)

    def message_del(
        self,
        msgid: Optional[int] = None
    ) -> Response:

        params = {
            'msgid': msgid
        }
        return self.query('messagedel', params)

    def message_get(
        self,
        msgid: Optional[int] = None
    ) -> Response:

        params = {
            'msgid': msgid
        }
        return self.query('messageget', params)

    def message_list(self) -> Response:
        return self.query('messagelist')

    def message_update_flag(
        self,
        msgid: Optional[int] = None,
        flag: Optional[int] = None
    ) -> Response:

        params = {
            'msgid': msgid,
            'flag': flag
        }
        return self.query('messageupdateflag', params)

    def perm_find(
        self,
        permid: Optional[int] = None,
        permsid: Optional[str] = None
    ) -> Response:

        params = {
            'permid': permid,
            'permsid': permsid
        }
        return self.query('permfind', params)

    def perm_get(
        self,
        permid: Optional[int] = None,
        permsid: Optional[str] = None
    ) -> Response:

        params = {
            'permid': permid,
            'permsid': permsid
        }
        return self.query('permget', params)

    def perm_id_get_by_name(
        self,
        permsid: Optional[str] = None
    ) -> Response:

        params = {
            'permsid': permsid
        }
        return self.query('permidgetbyname', params)

    def permission_list(self) -> Response:
        return self.query('permissionlist')

    def perm_overview(
        self,
        cid: Optional[int] = None,
        cldbid: Optional[int] = None,
        permid: Optional[int] = None,
        permsid: Optional[str] = None
    ) -> Response:

        params = {
            'cid': cid,
            'cldbid': cldbid,
            'permid': permid,
            'permsid': permsid
        }
        return self.query('permoverview', params)

    def perm_reset(self) -> Response:
        return self.query('permreset')

    def privilege_keya_dd(
        self,
        tokentype: Optional[int] = None,
        tokenid1: Optional[int] = None,
        tokendescription: Optional[str] = None,
        tokencustomset: Optional[str] = None
    ) -> Response:

        params = {
            'tokentype': tokentype,
            'tokenid1': tokenid1,
            'tokendescription': tokendescription,
            'tokencustomset': tokencustomset
        }
        return self.query('privilegekeyadd', params)

    def privilege_key_delete(
        self,
        token: Optional[str] = None
    ) -> Response:

        params = {
            'token': token
        }
        return self.query('privilegekeydelete', params)

    def privilege_key_list(self) -> Response:
        return self.query('privilegekeylist')

    def privilege_key_use(
        self,
        token: Optional[str] = None
    ) -> Response:

        params = {
            'token': token
        }
        return self.query('privilegekeyuse', params)

    def whoami(self) -> Response:
        return self.query('whoami')
        