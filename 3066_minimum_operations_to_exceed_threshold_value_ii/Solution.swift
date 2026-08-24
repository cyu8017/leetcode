// LeetCode 3066 - Minimum Operations to Exceed Threshold Value II
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

private struct MinHeap {
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
            if data[p] <= data[idx] { break }
            data.swapAt(p, idx)
            idx = p
        }
    }
    private mutating func siftDown(_ i: Int) {
        var idx = i
        while true {
            var smallest = idx
            let l = idx * 2 + 1, r = idx * 2 + 2
            if l < data.count && data[l] < data[smallest] { smallest = l }
            if r < data.count && data[r] < data[smallest] { smallest = r }
            if smallest == idx { break }
            data.swapAt(smallest, idx)
            idx = smallest
        }
    }
}

class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        var pq = MinHeap()
        for x in nums { pq.push(x) }
        var ans = 0
        while pq.count > 1 && pq.peek() < k {
            let x = pq.pop()
            let y = pq.pop()
            pq.push(x * 2 + y)
            ans += 1
        }
        return ans
    }
}
