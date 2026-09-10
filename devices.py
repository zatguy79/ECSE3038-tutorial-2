readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

x = 0
devices = ["name", "room", "temp", "online"]

def list_devices(T):
        for index, item in enumerate(readings):
            for key, value in readings[index].items():
                if key == T[0]:
                    print(f"{value}", end=" ")
                if key == T[2]:
                    print(f"{value}")   


def average_temp(R):
        temp = 0
        for index, item in enumerate(readings):
            for key, value in readings[index].items():
                if key == R[2]:
                    temp = temp + value 
        avg_temp = temp/len(readings)
        print(avg_temp)

def hottest(E):
        T_temp = 0
        for index, item in enumerate(readings):
            for key, value in readings[index].items():
                if key == E[2]:
                    if value > T_temp:
                        T_temp = value
                        T_temp_dict = readings[index]
        print(T_temp_dict)

list_devices(devices)

average_temp(devices)

hottest(devices)




