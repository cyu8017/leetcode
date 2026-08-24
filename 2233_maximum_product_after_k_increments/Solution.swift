// LeetCode 2233 - Maximum Product After K Increments
// https://leetcode.com/problems/maximum-product-after-k-increments/

private struct MinHeap {
    private var data: [Int] = []
    var isEmpty: Bool { data.isEmpty }
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
    func maximumProduct(_ nums: [Int], _ k: Int) -> Int {
        let mod = 1_000_000_007
        var h = MinHeap()
        for x in nums { h.push(x) }
        for _ in 0..<k {
            h.push(h.pop() + 1)
        }
        var ans = 1
        while !h.isEmpty {
            ans = ans * h.pop() % mod
        }
        return ans
    }
}
