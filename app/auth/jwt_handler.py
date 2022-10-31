import time , jwt

secret = "none"
algorithm = "HS256"

def token_response(token: str):
    return {
        'access_token': token
    }

def signJWT(userID: str):
    payload = {
        "userID": userID,
        "exp": time.time() + 600
    }

    token = jwt.encode(payload,secret,algorithm=algorithm)

    return token_response(token)

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, secret, algorithms=algorithm)
        return decoded_token if decoded_token["exp"] >= time.time() else None
    except:
        return {}
