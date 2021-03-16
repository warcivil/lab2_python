import json
import os
import threading


class readMyJsonLab():
    def json_read(self):
        with open(os.getcwd() + "\\lab1\\saveMyJson.json", 'r') as f:
            data = json.loads(f.read())
            return data

    def top_truency(self):  # метод, выводящий на экран топ 10 студентов
        self._data = self.json_read()
        for i in range(10):
            im = i
            for j in range(i + 1, len(self._data) - 1):
                if (self._data[im]["academic_perfomance"] <=
                        self._data[j]["academic_perfomance"]):
                    im = j
            t = self._data[im]
            self._data[im] = self._data[i]
            self._data[i] = t
            # swap(data i , data im)
        print("================]top 10 truancy[================")
        for i in range(10):
            print(i + 1, ". ", "user_id: ", self._data[i]["user_id"],
                  " academic perfomance: ",
                  self._data[i]["academic_perfomance"])
        print("================]top 10 truancy[================")

    def progulshiki(self):  # метод, выводящий на экран антитоп 10 студентов
        print("================]top 10 progulshiki[================")
        for i in range(len(self._data) - 1, len(self._data) - 10, -1):
            print(i + 1, ". ", "user_id: ", self._data[i]["user_id"],
                  " top progulshiki: ", self._data[i]["academic_perfomance"])
        print("================]top 10 progulshiki[================")

    def academic(self):
        data = self.json_read()
        discipline = {}

        for i in range(1000):
            if (data[i]["very_hard_discipline"] not in discipline):
                discipline[data[i]["very_hard_discipline"]] = 1
            else:
                discipline[data[i]["very_hard_discipline"]] += 1
        print("================]top 10 discipline[================")

        #list_d.sort(key=lambda i: i[1])

        list_items = list(discipline.items())
        list_items.sort(key=lambda i: i[1], reverse=True)
        bad_value = 1
        for i in list_items:
            print(str(bad_value) + ".", i[0], "->", i[1])
            bad_value += 1
            if (bad_value == 11):
                break

        print("================]top 10 discipline[================")

    def start(self,
              mutex=threading.Lock(),
              threadFlag=False):  # запуск 3 методов

        if (threadFlag):
            m = mutex.acquire()

        self.top_truency()
        self.academic()
        self.progulshiki()

        if (threadFlag):
            mutex.release()
