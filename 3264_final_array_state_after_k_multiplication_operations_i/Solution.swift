// LeetCode 3264 - Final Array State After K Multiplication Operations I
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

private struct MinHeap {
    private var data: [(Int, Int)] = []
    mutating func push(_ x: (Int, Int)) {
        data.append(x)
        siftUp(data.count - 1)
    }
    mutating func pop() -> (Int, Int) {
        let top = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(0)
        }
        return top
    }
    private func less(_ a: (Int, Int), _ b: (Int, Int)) -> Bool {
        a.0 != b.0 ? a.0 < b.0 : a.1 < b.1
    }
    private mutating func siftUp(_ i: Int) {
        var idx = i
        while idx > 0 {
            let p = (idx - 1) / 2
            if !less(data[idx], data[p]) { break }
            data.swapAt(p, idx)
            idx = p
        }
    }
    private mutating func siftDown(_ i: Int) {
        var idx = i
        while true {
            var smallest = idx
            let l = idx * 2 + 1, r = idx * 2 + 2
            if l < data.count && less(data[l], data[smallest]) { smallest = l }
            if r < data.count && less(data[r], data[smallest]) { smallest = r }
            if smallest == idx { break }
            data.swapAt(smallest, idx)
            idx = smallest
        }
    }
}

class Solution {
    func getFinalState(_ nums: [Int], _ k: Int, _ multiplier: Int) -> [Int] {
        var a = nums
        var h = MinHeap()
        for i in 0..<a.count { h.push((a[i], i)) }
        for _ in 0..<k {
            let (v, i) = h.pop()
            a[i] = v * multiplier
            h.push((a[i], i))
        }
        return a
    }
}
