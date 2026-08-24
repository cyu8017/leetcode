// LeetCode 2263 - Make Array Non-decreasing or Non-increasing
// https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/

private struct MaxHeap {
    private var data: [Int] = []
    var isEmpty: Bool { data.isEmpty }
    func peek() -> Int { data[0] }
    mutating func push(_ x: Int) {
        data.append(x)
        siftUp(data.count - 1)
    }
    mutating func pop() -> Int {
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
    func convertArray(_ nums: [Int]) -> Int {
        func cost(_ arr: [Int]) -> Int {
            var h = MaxHeap()
            var ans = 0
            for x in arr {
                if !h.isEmpty && h.peek() > x {
                    let t = h.pop()
                    ans += t - x
                    h.push(x)
                }
                h.push(x)
            }
            return ans
        }
        return min(cost(nums), cost(Array(nums.reversed())))
    }
}
