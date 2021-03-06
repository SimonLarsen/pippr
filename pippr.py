import time
import pickle

"""
"pips" er en liste der skal indeholder alle pip der er blevet skrevet.
Hvert pip skal været et dictionary der indeholder følgende tre felter:
    username: Brugernavnet på forfatteren af pippet. (str)
    text: Selve brødteksten for pippet. (str)
    time: Dato og klokkeslæt for pippet. (str)
"""
pips = [
    {"username": "admin", "text": "Dette er et test pip!", "time": "Wed Oct 11 12:34:48 2017"}
]

"""
"users" er et dictionary der indeholder alle registrerede brugere.
Hver nøgle er et brugernavn og den tilsværende værdi er et dictionary der indeholder følgende felter:
    name: Kaldenavn for brugeren. (str)
    password: Kodeord for brugeren. (str)
"""
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

Funktionen skal tilføje en ny brugere til "users" med det givne brugernavn, kaldenavn og kodeord.
Funktionen skal returnere False hvis der allerede eksisterer en bruger med dette navn
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

Funktionen skal tilføje et nyt pip til listen af pip.
Tidpunktet for tweetet er ikke givet - dette skal du selv tilføje.
Du kan få en streng med nuværende dato/klokkeslet med time.ctime().
Denne funktionen ikke returnere noget.

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

""" Indlæs persistent data.

Funktionen skal indlæse brugerdata og pips fra disken og gemme dem i "users"
og "pips" variablene. Hvis der ikke er noget data at læse skal funktionen
fortsætte uden at give en fejl.
Funktionen skal ikke returnere noget.
"""
def load_data():
    global users
    global pips
    try:
        users = pickle.load(open("users.pkl", "rb"))
        pips = pickle.load(open("pips.pkl", "rb"))
    except:
        print("No persistent data found.")

""" Gem persistent data.

Funktionen skal gemme brugerdata og pips til disken så de senere kan indlæses
med load_data().
Funktionen skal ikke returnere noget.
"""
def save_data():
    pickle.dump(users, open("users.pkl", "wb"))
    pickle.dump(pips, open("pips.pkl", "wb"))