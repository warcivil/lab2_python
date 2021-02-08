import pickle
from os import getcwd


class ReadPickleLab():
    def __init__(self):
        with open(getcwd() + '\\lab3\\data.pickle', 'rb') as f:
            self._data = pickle.load(f)

    def top_truency(self):  # метод, выводящий на экран топ 10 студентов
        top_laptop = dict()
        for i in self._data["model"]:
            if (i not in top_laptop):
                top_laptop[i] = 1
            else:
                top_laptop[i] += 1

        # print(top_laptop) sorted => top_laptop_cort
        top_laptop_cort = list(top_laptop.items())
        # Отсортировали и перевернули, получили кортеж топ ноутов по продажам
        top_laptop_cort.sort(key=lambda i: i[1], reverse=True)
        print()
        print("--------------best sell model--------------")
        for i in top_laptop_cort:
            print(i[0], ">", i[1], "sales")
            break  # я понимаю что это полная ерунда, но я не хотел переделывать
        print("--------------best sell model--------------")

    def very_effectly_user(self):
        top_user_effect = list(self._data["user"].items())
        top_user_effect.sort(key=lambda i: i[1], reverse=True)
        # print(top_user_effect)
        print()
        print("--------------best effect user--------------")
        for i in top_user_effect:
            print(i[0], ">", i[1], "%", "efficiency")
            break  # аналогично
        print("--------------best effect user--------------")
        print()

    def top_gpu(self):
        top_gpu_expensive = list(self._data["gpu"].items())
        top_gpu_expensive.sort(key=lambda i: i[1], reverse=True)
        # print(top_user_effect)
        print()
        print("--------------best expensive gpu--------------")
        badCounter = 0
        for i in top_gpu_expensive:
            if (badCounter < 5):
                print(i[0], ">", i[1], "€", "price")
            else:
                break  # аналогично
        print("--------------best expensive gpu--------------")
        print()

    def start(self):
        self.top_truency()
        self.very_effectly_user()
        self.top_gpu()


if __name__ == '__main__':
    m = ReadPickleLab()
    m.start()
    m.top_truency()
