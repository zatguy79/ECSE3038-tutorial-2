readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]
x = 0
devices = ["name", "temp"]
def list_devices(T):
        for index, item in enumerate(readings):
            for key, value in readings[index].items():
                if key == T[0]:
                    print(f"{value}", end=" ")
                if key == T[1]:
                    print(f"{value}")   

list_devices(devices)


