import multiprocessing  # импорт библиотек и скриптов для работф
import lab1.readMyJson
import lab1.saveMyJson  # lab1
import lab2.readMyJson1  # lab2
import lab2.saveMyJson1
import lab3.savePickle
import lab3.readPickle  # lab3
import threading  # потоки
import signal, os


class StarterLab12():  # запуск лаб
    def __init__(self, read_my_json,
                 save_my_json):  # конструктор для запуска файлов
        self._mutex = threading.Lock()
        try:
            self._user_info = read_my_json.readMyJsonLab()
            self._saveMyJson = save_my_json.SimpleSaverJsonFile()
        except:  # выбор между тремя лабами в 1 и 2 лабе классы названы одинаково, а в 3 по другому
            self._user_info = read_my_json.ReadPickleLab()
            self._saveMyJson = save_my_json.savePickle()

    def threader(self):  # потоки

        thread2 = threading.Thread(target=self._saveMyJson.start,
                                   args=[self._mutex, True])  # saveMyJson
        thread1 = threading.Thread(target=self._user_info.start,
                                   args=[self._mutex, True])  # readMyJson
        self._mutex.acquire(
        )  # блокируем потоки ожидаем анлока мютекса в savefile
        thread2.start()
        thread1.start()
        thread2.join()
        thread1.join()

    def proccess(self):  # процессы
        proc = multiprocessing.Process(target=self._user_info.start())
        proc.start()
        proc.join()
        proc.terminate()

        proc1 = multiprocessing.Process(target=self._saveMyJson.start())
        proc1.start()
        proc1.join()
        proc1.terminate()

    def timer(self):  # таймер
        self._saveMyJson.start()
        threading.Timer(
            5, self._user_info.start).start()  # запуск после 5 секунды

    def start(self):
        '''
         cтарт выборка между вариантами запуска, 
         как бонус, прогу можно запустить всеми 3 методами, 
         как минус, я мог написать что-то неправильно
        '''
        while True:
            n = input("запуск через потоки или процессы или таймер? ")

            while (n != "потоки" and n != "процессы" and n != "таймер"):
                print("ошибка в вводе повторите еще раз")
                n = input("запуск через потоки или процессы или таймер?")
            print(n)
            #   print(n != "процессы")
            if (n == "процессы"):
                self.proccess()

            elif (n == "потоки"):
                self.threader()
            elif (n == "таймер"):
                self.timer()


if __name__ == "__main__":
    while True:
        n = input("lab1 или lab2 или lab3 ")
        if (n in ["lab1", "lab2", "lab3"]):
            break
    if (n == "lab1"):
        start = StarterLab12(lab1.readMyJson, lab1.saveMyJson)
        start.start()
    elif (n == "lab2"):
        start = StarterLab12(lab2.readMyJson1, lab2.saveMyJson1)
        start.start()
    elif (n == "lab3"):
        start = StarterLab12(lab3.readPickle, lab3.savePickle)
        start.start()
