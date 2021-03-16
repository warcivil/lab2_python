import json
from os import getcwd
from threading import Lock


class readMyJsonLab():
    def json_read(self):
        with open(getcwd() + "\\lab2\\saveMyJson.json", 'r') as f:
            _data = json.loads(f.read())
            return _data

    def top_price_spare_part(self):
        _data = self.json_read()
        for i in range(5):
            im = i
            for j in range(i + 1, 1000):
                if (_data[im]["price spare part"] <=
                        _data[j]["price spare part"]):
                    im = j
            t = _data[im]
            _data[im] = _data[i]
            _data[i] = t
            # swap(data i , data im)
        print("================]top 5 truancy[================")
        for i in range(5):
            print(i + 1, ". ", "user_id: ", _data[i]["user_id"],
                  " spire part: ", _data[i]["most expensive spare part"],
                  "price spart part", _data[i]["price spare part"])
        print("================]top 5 truancy[================")

    def five_auto(self):
        _data = self.json_read()
        discipline = {}

        for i in range(1000):
            if (_data[i]["automobile"] not in discipline):
                discipline[_data[i]["automobile"]] = 1
            else:
                discipline[_data[i]["automobile"]] += 1
        print("================]top 5 automobile[================")

        #list_d.sort(key=lambda i: i[1])

        list_items = list(discipline.items())
        list_items.sort(key=lambda i: i[1], reverse=True)
        bad_value = 1
        for i in list_items:
            print(bad_value, ".", i[0], "->", i[1])
            bad_value += 1
            if (bad_value == 6):
                break

        print("================]top 5 automobile[================")

    def start(self, mutex=Lock(), threadFlag=False):
        if (threadFlag):
            mutex.acquire()
        self.top_price_spare_part()
        self.five_auto()
        if (threadFlag):
            mutex.release()


if __name__ == '__main__':
    m = readMyJsonLab()
    m.start()