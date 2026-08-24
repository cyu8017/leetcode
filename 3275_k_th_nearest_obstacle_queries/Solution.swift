// LeetCode 3275 - K-th Nearest Obstacle Queries
// https://leetcode.com/problems/k-th-nearest-obstacle-queries/

private struct MaxHeap {
    private var data: [Int] = []
    var count: Int { data.count }
    func peek() -> Int { data[0] }
    mutating func push(_ x: Int) {
        data.append(x)
        siftUp(data.count - 1)
    }
    mutating func pop() -> Int {
        let top = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(0)
        }
        return top
    }
    private mutating func siftUp(_ i: Int) {
        var idx = i
        while idx > 0 {
            let p = (idx - 1) / 2
            if data[p] >= data[idx] { break }
            data.swapAt(p, idx)
            idx = p
        }
    }
    private mutating func siftDown(_ i: Int) {
        var idx = i
        while true {
            var largest = idx
            let l = idx * 2 + 1, r = idx * 2 + 2
            if l < data.count && data[l] > data[largest] { largest = l }
            if r < data.count && data[r] > data[largest] { largest = r }
            if largest == idx { break }
            data.swapAt(largest, idx)
            idx = largest
        }
    }
}

class Solution {
    func resultsArray(_ queries: [[Int]], _ k: Int) -> [Int] {
        var h = MaxHeap()
        return queries.map { q in
            h.push(abs(q[0]) + abs(q[1]))
            if h.count > k { _ = h.pop() }
            return h.count < k ? -1 : h.peek()
        }
    }
}
