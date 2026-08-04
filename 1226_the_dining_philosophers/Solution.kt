// LeetCode 1226 - The Dining Philosophers
// https://leetcode.com/problems/the-dining-philosophers/

import java.util.concurrent.locks.ReentrantLock

class DiningPhilosophers {
    private val forks = Array(5) { ReentrantLock() }

    fun wantsToEat(
        philosopher: Int,
        pickLeftFork: Runnable,
        pickRightFork: Runnable,
        eat: Runnable,
        putLeftFork: Runnable,
        putRightFork: Runnable
    ) {
        val left = philosopher
        val right = (philosopher + 1) % 5
        val first = if (philosopher % 2 == 0) left else right
        val second = if (philosopher % 2 == 0) right else left
        forks[first].lock()
        forks[second].lock()
        try {
            pickLeftFork.run()
            pickRightFork.run()
            eat.run()
            putLeftFork.run()
            putRightFork.run()
        } finally {
            forks[second].unlock()
            forks[first].unlock()
        }
    }
}
