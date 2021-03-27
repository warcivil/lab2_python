import os
from datetime import datetime
from mimetypes import guess_type

with open("pass.txt", "r") as f:
    date = f.read().split(" ")

info = input().split(" ")
userAuth = True if "auth" in info and date[0] == info[1] and date[1] == info[
    2] else False
while userAuth:
    command = input().split(" ")
    if (command[0] == "list"):
        for root, dirs, files in os.walk("."):
            for filename in files:
                print(filename)
    elif (command[0] == "info"):
        try:
            print(
                "дата создания: ",
                datetime.fromtimestamp(
                    os.path.getmtime(os.getcwd() + "/" + command[1])))
            print("MIME тип:", guess_type(os.getcwd() + " / " + command[1]))
            print("тип файла:", command[1].split(".")[1])
        except:
            print("такого файла нет")
    elif (command[0] == "exit"):
        print("bye bye")
        break
