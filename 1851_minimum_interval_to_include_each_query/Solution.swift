// LeetCode 1851 - Minimum Interval to Include Each Query
// https://leetcode.com/problems/minimum-interval-to-include-each-query/

private struct IntervalHeapItem: Comparable {
    let size: Int
    let right: Int

    static func < (lhs: IntervalHeapItem, rhs: IntervalHeapItem) -> Bool {
        if lhs.size != rhs.size { return lhs.size < rhs.size }
        return lhs.right < rhs.right
    }
}

private struct MinHeap {
    private var data: [IntervalHeapItem] = []

    var isEmpty: Bool { data.isEmpty }

    mutating func peek() -> IntervalHeapItem {
        data[0]
    }

    mutating func push(_ item: IntervalHeapItem) {
        data.append(item)
        siftUp(data.count - 1)
    }

    mutating func pop() -> IntervalHeapItem {
        let top = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(0)
        }
        return top
    }

    private mutating func siftUp(_ index: Int) {
        var idx = index
        while idx > 0 {
            let parent = (idx - 1) / 2
            if data[parent] <= data[idx] { break }
            data.swapAt(parent, idx)
            idx = parent
        }
    }

    private mutating func siftDown(_ index: Int) {
        var idx = index
        while true {
            let left = idx * 2 + 1
            let right = left + 1
            var smallest = idx
            if left < data.count && data[left] < data[smallest] {
                smallest = left
            }
            if right < data.count && data[right] < data[smallest] {
                smallest = right
            }
            if smallest == idx { break }
            data.swapAt(idx, smallest)
            idx = smallest
        }
    }
}

class Solution {
    func minInterval(_ intervals: [[Int]], _ queries: [Int]) -> [Int] {
        let sortedIntervals = intervals.sorted { $0[0] < $1[0] }
        let indexedQueries = queries.enumerated().sorted { $0.element < $1.element }
        var heap = MinHeap()
        var answer = Array(repeating: -1, count: queries.count)
        var intervalIdx = 0

        for (queryIdx, query) in indexedQueries {
            while intervalIdx < sortedIntervals.count && sortedIntervals[intervalIdx][0] <= query {
                let left = sortedIntervals[intervalIdx][0]
                let right = sortedIntervals[intervalIdx][1]
                heap.push(IntervalHeapItem(size: right - left + 1, right: right))
                intervalIdx += 1
            }

            while !heap.isEmpty && heap.peek().right < query {
                _ = heap.pop()
            }

            if !heap.isEmpty {
                answer[queryIdx] = heap.peek().size
            }
        }

        return answer
    }
}
