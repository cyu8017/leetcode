// LeetCode 2349 - Design a Number Container System
// https://leetcode.com/problems/design-a-number-container-system/

class NumberContainers {
    private var idx: [Int: Int] = [:]
    private var heap: [Int: Set<Int>] = [:]

    init() {}

    func change(_ index: Int, _ number: Int) {
        idx[index] = number
        heap[number, default: []].insert(index)
    }

    func find(_ number: Int) -> Int {
        guard var h = heap[number] else { return -1 }
        while let i = h.min() {
            if idx[i] == number { return i }
            h.remove(i)
        }
        heap[number] = h
        return -1
    }
}
