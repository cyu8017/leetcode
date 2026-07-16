// LeetCode 0218 - The Skyline Problem
// https://leetcode.com/problems/the-skyline-problem/

import Foundation

private struct HeapItem: Comparable {
    let negH: Int
    let end: Int

    static func < (lhs: HeapItem, rhs: HeapItem) -> Bool {
        lhs.negH < rhs.negH
    }
}

private struct MinHeap {
    private var data: [HeapItem] = []

    var isEmpty: Bool { data.isEmpty }

    mutating func peek() -> HeapItem {
        data[0]
    }

    mutating func push(_ item: HeapItem) {
        data.append(item)
        siftUp(data.count - 1)
    }

    mutating func pop() -> HeapItem {
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
            if data[parent] <= data[idx] {
                break
            }
            data.swapAt(parent, idx)
            idx = parent
        }
    }

    private mutating func siftDown(_ index: Int) {
        var idx = index
        while true {
            var smallest = idx
            let left = idx * 2 + 1
            let right = idx * 2 + 2
            if left < data.count && data[left] < data[smallest] {
                smallest = left
            }
            if right < data.count && data[right] < data[smallest] {
                smallest = right
            }
            if smallest == idx {
                break
            }
            data.swapAt(smallest, idx)
            idx = smallest
        }
    }
}

class Solution {
    func getSkyline(_ buildings: [[Int]]) -> [[Int]] {
        var events: [(Int, Int, Int)] = []
        for building in buildings {
            events.append((building[0], -building[2], building[1]))
            events.append((building[1], 0, 0))
        }
        events.sort { lhs, rhs in
            if lhs.0 != rhs.0 {
                return lhs.0 < rhs.0
            }
            return lhs.1 < rhs.1
        }

        var result: [[Int]] = []
        var live = MinHeap()
        live.push(HeapItem(negH: 0, end: Int.max))

        for (x, negH, end) in events {
            while live.peek().end <= x {
                _ = live.pop()
            }
            if negH != 0 {
                live.push(HeapItem(negH: negH, end: end))
            }
            let height = -live.peek().negH
            if result.isEmpty || result[result.count - 1][1] != height {
                result.append([x, height])
            }
        }
        return result
    }
}
