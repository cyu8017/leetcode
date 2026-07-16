from threading import Lock
from typing import Callable

class TrafficLight:
    def __init__(self):
        self.green_road = 1
        self.lock = Lock()

    def carArrived(self, carId: int, roadId: int, direction: int,
                   turnGreen: "Callable", crossCar: "Callable") -> None:
        with self.lock:
            if roadId != self.green_road:
                turnGreen()
                self.green_road = roadId
            crossCar()
