class SetBasicXmlInfoVo:

    def __init__(self, url, authId, authKey):
        self._url = url
        self._authId = authId
        self._authKey = authKey

    def __int__(self, url, prop_id, authId, authKey):
        self._url = url
        self._prop_id = prop_id
        self._authId = authId
        self._authKey = authKey

    def getUrl(self):
        return self._url

    def getPropId(self):
        return self._prop_id

    def getAuthId(self):
        return self._authId

    def getAuthKey(self):
        return self._authKey