// LeetCode 1226 - The Dining Philosophers
// https://leetcode.com/problems/the-dining-philosophers/

import java.util.concurrent.locks.ReentrantLock;

class DiningPhilosophers {
    private final ReentrantLock[] forks = new ReentrantLock[5];

    public DiningPhilosophers() {
        for (int i = 0; i < 5; i++) forks[i] = new ReentrantLock();
    }

    public void wantsToEat(int philosopher, Runnable pickLeftFork, Runnable pickRightFork,
                           Runnable eat, Runnable putLeftFork, Runnable putRightFork) throws InterruptedException {
        int left = philosopher, right = (philosopher + 1) % 5;
        int first = philosopher % 2 == 0 ? left : right;
        int second = philosopher % 2 == 0 ? right : left;
        forks[first].lock();
        forks[second].lock();
        try {
            pickLeftFork.run();
            pickRightFork.run();
            eat.run();
            putLeftFork.run();
            putRightFork.run();
        } finally {
            forks[second].unlock();
            forks[first].unlock();
        }
    }
}

