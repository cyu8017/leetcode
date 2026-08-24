// LeetCode 0641 - Design Circular Deque
// https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque {
    private var data: [Int]
    private let capacity: Int
    private var front = 0
    private var size = 0

    init(_ k: Int) {
        data = Array(repeating: 0, count: k)
        capacity = k
    }

    func insertFront(_ value: Int) -> Bool {
        if isFull() { return false }
        front = (front - 1 + capacity) % capacity
        data[front] = value
        size += 1
        return true
    }

    func insertLast(_ value: Int) -> Bool {
        if isFull() { return false }
        data[(front + size) % capacity] = value
        size += 1
        return true
    }

    func deleteFront() -> Bool {
        if isEmpty() { return false }
        front = (front + 1) % capacity
        size -= 1
        return true
    }

    func deleteLast() -> Bool {
        if isEmpty() { return false }
        size -= 1
        return true
    }

    func getFront() -> Int { isEmpty() ? -1 : data[front] }

    func getRear() -> Int {
        if isEmpty() { return -1 }
        return data[(front + size - 1) % capacity]
    }

    func isEmpty() -> Bool { size == 0 }
    func isFull() -> Bool { size == capacity }
}
