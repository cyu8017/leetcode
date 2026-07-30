// LeetCode 1226 - The Dining Philosophers
// https://leetcode.com/problems/the-dining-philosophers/

using System;

public class DiningPhilosophers {
    private readonly object[] forks = new object[5];

    public DiningPhilosophers() {
        for (int i = 0; i < 5; i++) forks[i] = new object();
    }

    public void WantsToEat(int philosopher, Action pickLeftFork, Action pickRightFork,
                           Action eat, Action putLeftFork, Action putRightFork) {
        int left = philosopher;
        int right = (philosopher + 1) % 5;
        int first = philosopher % 2 == 0 ? left : right;
        int second = philosopher % 2 == 0 ? right : left;
        lock (forks[first]) {
            lock (forks[second]) {
                pickLeftFork();
                pickRightFork();
                eat();
                putLeftFork();
                putRightFork();
            }
        }
    }
}
