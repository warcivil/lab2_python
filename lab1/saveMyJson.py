import json
import threading
import random
import time
from os import getcwd


class SimpleSaverJsonFile():
    def generate(self):  # генерация предметов
        a = [
            "math", "rocket science", "history", "sport", "physics",
            "philosophy", "unix course", "python", "java", "greenfield", "tez",
            "dota cybersport", "electronics", "doctor course",
            "stepik base system"
        ]
        return a[random.randint(0, len(a) - 1)]

    def json_dump(self,
                  dateForJson):  # открываем в формате сохранения файл .json
        with open(getcwd() + '\\lab1\\saveMyJson.json', "w",
                  encoding="utf-8") as file:
            json.dump(dateForJson, file)

    def start(self):  # генерация json
        dateForJson = []

        for _ in range(1000):
            dateForJson.append({
                "user_id":
                random.randint(1, 99999999),
                "couples_skipped":
                random.randint(1, 10),
                "academic_perfomance":
                round(random.uniform(1, 5), 3),
                "very_hard_discipline":
                self.generate()
            })

        self.json_dump(dateForJson)