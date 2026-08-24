// LeetCode 2386 - Find the K-Sum of an Array
// https://leetcode.com/problems/find-the-k-sum-of-an-array/

private struct HeapNode: Comparable {
    let sum: Int
    let i: Int
    static func < (lhs: HeapNode, rhs: HeapNode) -> Bool { lhs.sum < rhs.sum }
}

private struct MaxHeap {
    private var data: [HeapNode] = []
    func peek() -> HeapNode { data[0] }
    mutating func push(_ x: HeapNode) {
        data.append(x)
        siftUp(data.count - 1)
    }
    mutating func pop() -> HeapNode {
        let top = data[0]
        let last = data.removeLast()
        if !data.isEmpty { data[0] = last; siftDown(0) }
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
    func kSum(_ nums: [Int], _ k: Int) -> Int {
        var total = 0
        var absNums = nums.map { x -> Int in
            if x >= 0 { total += x; return x }
            return -x
        }.sorted()
        var h = MaxHeap()
        h.push(HeapNode(sum: total, i: 0))
        if k > 1 {
            for _ in 0..<(k - 1) {
                let cur = h.pop()
                if cur.i >= absNums.count { continue }
                h.push(HeapNode(sum: cur.sum - absNums[cur.i], i: cur.i + 1))
                if cur.i > 0 {
                    h.push(HeapNode(sum: cur.sum - absNums[cur.i] + absNums[cur.i - 1], i: cur.i + 1))
                }
            }
        }
        return h.peek().sum
    }
}
