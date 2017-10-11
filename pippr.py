import time

pips = [
    {"username": "admin", "text": "Dette er et test pip!", "time": "Wed Oct 11 12:34:48 2017"}
]

users = {
    "admin": { "name": "Admin", "password": "test123"}
}

""" Check om en bruger bruger er registreret.

Funktionen skal returnere True hvis der findes en bruger med dette kodeord og brugernavn
og returnere False hvis brugeren ikke findes eller hvis kodeordet er forkert.

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

Funktionen skal tilføje en ny brugere til "users" med de givne brugernavn, navn og kodeord.
Funktionen skal returnere returnere False hvis der allerede eksisterer en bruger med dette navn
eller returnere True hvis brugeren blev oprettet uden problemer.

Argumenter:
    username: Brugernavn for ny bruger.
    name: Kaldenavn for ny bruger.
    password: Kodeord for ny bruger.
"""
def register_user(username, name, password):
    if username in users:
        return False
    users[username] = {"name": name, "password": password}
    return True

""" Tilføj et nyt pip til databasen.

Funktionen skal tilføje et nyt pip til listen af pips.
Skal ikke returnere noget.

Argumenter:
    username: Brugernavn for forfatteren af det nye pip.
    text: Brødteksten for det nye pip.
"""
def post_pip(username, text):
    ctime = time.ctime()
    pips.append({"username": username, "text": text, "time": ctime})

""" Returner kaldenavn for bruger.

Givet et brugernavn skal funktionen returnere den tilsvarende brugers kaldenavn.

Argumenter:
    username: Brugernavn for brugeren.
"""
def get_name(username):
    return users[username]["name"]

""" Returner de seneste pips.

Funktionen skal returnere en liste med de seneste "count" pip i rækkefølge fra ældst til nyest.

Argumenter:
    count: En integer der fortæller hvor mange pips der skal returneres.
"""
def get_recent_pips(count):
    return pips[-count:]

""" Returner alle pip skrevet af specifik bruger.

Funktionen skal returnere en liste med alle de pip der er skrevet af en specifik bruger i rækkefølge fra ældst til nyest.

Argumenter:
    username: Brugernavn for brugeren hvis pip skal returneres.
"""
def get_user_pips(username):
    return [t for t in pips if t["username"] == username]

""" Returner alle tweets der nævner en bruger.

Funktionen skal returnere en liste med alle de pip der nævner en specifik bruger, dvs. pippets tekst indeholder "@username". Skal returneres i rækkefølge fra ældst til nyest.

Argumenter:
    username: Brugernavn for bruger der skal være nævnt.
"""
def get_mentions(username):
    return [t for t in pips if username in t["text"]]

""" Returner alle tweets der indeholder søgestrengen "text".

Funktionen skal returnere en liste med alle de pip der indeholder en søgetekst i rækkefølge fra ældst til nyest.

Argumenter:
    text: Søgetekst der skal søges efter.
"""
def search_pips(text):
    return [t for t in pips if text in t["text"]]
