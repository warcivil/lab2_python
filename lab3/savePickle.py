import pickle
from random import randint
from os import getcwd


class savePickle():
    def __init__(self):
        self._gpu = []
        self._price = []
        self._user = []
        self._model = []

    def gen_user(self) -> str:  # генерация user_id
        return "user_" + str(randint(0, 10**9))

    def gen_gpu(self):  # генерация товаров видеокарт
        t = [
            "nvidia 2060rtx", "nvidia 2070rtx", "nvidia 3080rtx",
            "nvidia 3090rtx", "nvidia 1660 gtx", "amd 580gx", "amd 580gx"
        ]
        return t[randint(0, len(t) - 1)]

    def gen_model(self) -> str:  # генерация моделей ноутбука
        return "model_" + str(randint(1, 20))

    def start(self):  # генерируем пикл файл

        self._price = [randint(0, 100) for i in range(40)]
        self._user = dict()
        self._gpu = dict()
        for _ in range(
                40):  # у каждого юзера есть эффективность, у каждой гпу - цена
            self._user[self.gen_user()] = randint(1, 99)
            self._gpu[self.gen_gpu()] = randint(1, 10000)
        self._model = [self.gen_model() for i in range(40)]
        self._data = {
            "gpu": self._gpu,
            "price": self._price,
            "user": self._user,
            "model": self._model
        }
        self.write(self._data)

    def write(self, data):  # запись в файл
        with open(getcwd() + '\\lab3\\data.pickle', 'wb') as f:
            pickle.dump(data, f)

    def read(
        self
    ):  #  чтение файла, создавалось исключительно для тестирования работоспособности скрипта
        with open(getcwd() + '\\lab3\\data.pickle', 'rb') as f:
            return pickle.load(f)


if __name__ == "__main__":
    m = savePickle()
    m.start()
    print(m.read())
