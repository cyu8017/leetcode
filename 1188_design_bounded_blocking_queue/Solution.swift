// LeetCode 1188 - Design Bounded Blocking Queue
// https://leetcode.com/problems/design-bounded-blocking-queue/

import Foundation

class BoundedBlockingQueue {
    private let capacity: Int
    private var q: [Int] = []
    private let lock = NSCondition()

    init(_ capacity: Int) {
        self.capacity = capacity
    }

    func enqueue(_ element: Int) {
        lock.lock()
        while q.count == capacity {
            lock.wait()
        }
        q.append(element)
        lock.broadcast()
        lock.unlock()
    }

    func dequeue() -> Int {
        lock.lock()
        while q.isEmpty {
            lock.wait()
        }
        let v = q.removeFirst()
        lock.broadcast()
        lock.unlock()
        return v
    }

    func size() -> Int {
        lock.lock()
        let s = q.count
        lock.unlock()
        return s
    }
}
