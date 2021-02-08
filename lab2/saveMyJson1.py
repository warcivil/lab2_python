import json
import random
from os import getcwd


class SimpleSaverJsonFile():
    def generate_spare_part(self):
        a = [
            "Generator", "Ball", "wheels", "engine", "Brake discs",
            "carburetor", "injector"
        ]
        return a[random.randint(0, len(a) - 1)]

    def generate_auto(self):
        a = [
            "mercedes bens", "cherry tiggo 8", "wolfswagen golf",
            "lada kalina", "lada largus", "lamborghini", "bugatti",
            "range rover", "toyota corolla", "toyota prado", "HAVAL",
            "MITSUBISHI LANCER", "toyota supra", "toyota corolla", "craisler"
        ]
        return a[random.randint(0, len(a) - 1)]

    def json_dump(self, dateForJson):
        with open(getcwd() + "\\lab2\\saveMyJson.json", "w",
                  encoding="utf-8") as file:
            json.dump(dateForJson, file)

    def start(self):
        _dateForJson = []

        for _ in range(1000):
            _dateForJson.append({
                "user_id":
                random.randint(1, 99999999),
                "automobile":
                self.generate_auto(),
                "most expensive spare part":
                self.generate_spare_part(),
                "price spare part":
                round(random.uniform(290, 1454), 3)
            })

        self.json_dump(_dateForJson)


if __name__ == "__main__":
    m = SimpleSaverJsonFile()
    m.go_json()