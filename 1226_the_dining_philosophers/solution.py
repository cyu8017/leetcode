from threading import Lock

class DiningPhilosophers:
    def __init__(self):
        self.forks = [Lock() for _ in range(5)]

    def wantsToEat(self, philosopher: int, pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]', eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]', putRightFork: 'Callable[[], None]') -> None:
        left, right = philosopher, (philosopher + 1) % 5
        first, second = (left, right) if philosopher % 2 == 0 else (right, left)
        with self.forks[first]:
            with self.forks[second]:
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()
