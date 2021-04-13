import os
import os
from datetime import datetime
from mimetypes import guess_type
import shutil

with open("user.txt", "r") as f:
    date = f.read().replace(" ", "_")
    date = date.replace("\n", "_")
    date = date.split("_")
info = input().replace(" ", "_")
info = info.replace("\n", "_")
info = info.split("_")
userAuth = True if "auth" in info and info[1] in date and info[
    2] in date else False
while (not userAuth):
    print("bad login")
    info = input().split("_")
    userAuth = True if "auth" in info and info[1] in date and info[
        2] in date else False

while userAuth:
    command = input("Введите команду ").split(" ")
    if (command[0] == "list"):
        try:
            with open(os.getcwd() + "/" + "msg/" + info[1] + "_" + info[2],
                      'r') as file:
                print(file.read())
        except:
            print("no message")
    elif (command[0] == "read"):
        with open(os.getcwd() + "/" + "msg" + "/" + command[1], "r") as file:
            print(file.read())

    elif (command[0] == "send"):
        title = input("тема: ")
        message = input("сообщение: ")
        with open(os.getcwd() + "/" + "msg" + "/" + command[1], "a") as file:
            file.write("--------title--------")
            file.write("\n" + title.split(".")[0])
            file.write("\n--------title--------\n")
            file.write("\n-------message-------")
            file.write("\n" + message.split(".")[0])
            file.write("\n-------message-------\n")
            with open("user.txt", "r") as b:
                if (command[1] not in b.read()):
                    with open("user.txt", "a") as f:
                        f.write("\n" + command[1])

    elif (command[0] == "exit"):
        print("bye bye")
        break
    elif (command[0] == "help"):
        print(
            "auth user pass — авторизация\n"
            "list — показать список сообщений\n"
            "read msg — вывести сообщение под номером msg\n"
            "send user — ввод сообщения для пользователя. Запрашиватеся тема, ввод заканчивается одиночным символом «.»\n"
            "exit — выход")