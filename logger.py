import datetime
import random
import time

users = ["user", "qwerty123", "no_name", "vasya", "petya", "tourist", "um_nik", "tsar228", "asdf", "lol", "kek"]
folders = ["users", "films", "books", "music", "documents", "pictures", "prikazi_ob_otchislenii", "code"]

while (True):
    file = open("log.txt", "a")

    type = random.randint(0, 2)
    status = 0
    user = users[random.randint(0, len(users) - 1)]
    request_time = random.randint(1, 100)
    severity = ""
    path = "/api/" + folders[random.randint(0, len(folders) - 1)]

    if (type == 0):
        severity = "INFO"
        status = 200 + random.randint(0, 9)
    elif (type == 1):
        severity = "WARN"
        status = 400 + random.randint(0, 99)
    else:
        severity = "ERROR"
        status = 500 + random.randint(0, 99)


    file.write(str(datetime.date.today()) + " " + severity + " " + str(status) + " " + user + " " + str(request_time) + " " + path + "\n")

    file.close()
    time.sleep(10)

