// LeetCode 1226 - The Dining Philosophers
// https://leetcode.com/problems/the-dining-philosophers/

import Foundation

class DiningPhilosophers {
    private let locks: [NSLock] = (0..<5).map { _ in NSLock() }

    func wantsToEat(
        _ philosopher: Int,
        _ pickLeftFork: () -> Void,
        _ pickRightFork: () -> Void,
        _ eat: () -> Void,
        _ putLeftFork: () -> Void,
        _ putRightFork: () -> Void
    ) {
        let left = philosopher
        let right = (philosopher + 1) % 5
        let first = min(left, right)
        let second = max(left, right)
        locks[first].lock()
        locks[second].lock()
        pickLeftFork(); pickRightFork(); eat()
        putLeftFork(); putRightFork()
        locks[second].unlock()
        locks[first].unlock()
    }
}
