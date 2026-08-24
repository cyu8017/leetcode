// LeetCode 0622 - Design Circular Queue
// https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue {
    private var data: [Int]
    private let capacity: Int
    private var head = 0
    private var size = 0

    init(_ k: Int) {
        data = Array(repeating: 0, count: k)
        capacity = k
    }

    func enQueue(_ value: Int) -> Bool {
        if isFull() { return false }
        data[(head + size) % capacity] = value
        size += 1
        return true
    }

    func deQueue() -> Bool {
        if isEmpty() { return false }
        head = (head + 1) % capacity
        size -= 1
        return true
    }

    func Front() -> Int { isEmpty() ? -1 : data[head] }

    func Rear() -> Int {
        if isEmpty() { return -1 }
        return data[(head + size - 1) % capacity]
    }

    func isEmpty() -> Bool { size == 0 }
    func isFull() -> Bool { size == capacity }
}
