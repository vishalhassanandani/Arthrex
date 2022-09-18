def credentials(usrrname: str, password: str) -> dict:
    credentials: dict = {}
    credentials.__setitem__('username', usrrname)
    credentials.__setitem__('password', password)
    return credentials
