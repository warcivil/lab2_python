import os
import os
from datetime import datetime
from mimetypes import guess_type
import shutil

with open("user.txt", "r") as f:
    date = f.read().split(" ")

info = input().split(" ")
userAuth = True if "auth" in info and date[0] == info[1] and date[1] == info[
    2] else False
while userAuth:
    command = input("Введите команду ").split(" ")
    if (command[0] == "list"):
        for root, dirs, files in os.walk("msg"):
            for filename in files:
                print(filename)
    elif (command[0] == "read"):
        with open(os.getcwd() + "/" + "msg" + "/" + command[1] + ".txt",
                  "r") as file:
            print(file.read())

    elif (command[0] == "send"):
        title = input("тема: ")
        message = input("сообщение: ")
        with open(os.getcwd() + "/" + "msg" + "/" + command[1] + ".txt",
                  "w") as file:
            file.write("--------title--------")
            file.write("\n" + title.split(".")[0])
            file.write("\n--------title--------\n")
            file.write("\n-------message-------")
            file.write("\n" + message.split(".")[0])
            file.write("\n-------message-------\n")
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