import time

pips = [
    {"username": "admin", "text": "Dette er et test pip!", "time": "Wed Oct 11 12:34:48 2017"}
]

users = {
    "admin": { "name": "Admin", "password": "test123"}
}

""" Check om en bruger bruger er registreret.

Funktion skal returnere True hvis der findes en bruger med dette kodeord og brugernavn.
Returner False hvis brugeren ikke findes eller hvis kodeordet er forkert.

Argumenter:
    users: Liste af brugere. Hver bruger er et dictionary der indeholder nøglerne "username" og "password".
    username: Brugernavn for bruger.
    password: Kodeord for bruger.
"""
def check_user(username, password):
    if username in users:
        if users[username]["password"] == password:
            return True
    return False

""" Registrer ny bruger.
"""
def register_user(username, name, password):
    if username in users:
        return False
    users[username] = {"name": name, "password": password}
    return True

""" Tilføj et nyt pip til databasen.
"""
def post_pip(username, text):
    ctime = time.ctime()
    pips.append({"username": username, "text": text, "time": ctime})

""" Returner kaldenavn for bruger.
"""
def get_name(username):
    return users[username]["name"]

""" Returner de seneste pips.
"""
def get_recent_pips(count):
    return pips[:-(count+1):-1]

""" Returner alle pips skrevet af specifik bruger.
"""
def get_user_pips(username):
    return [t for t in pips[::-1] if t["username"] == username]

""" Returner alle tweets der nævner en bruger.
"""
def get_mentions(username):
    return [t for t in pips[::-1] if username in t["text"]]

""" Returner alle tweets der indeholder søgestrengen "text".
"""
def search_pips(text):
    return [t for t in pips[::-1] if text in t["text"]]
