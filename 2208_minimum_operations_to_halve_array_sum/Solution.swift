// LeetCode 2208 - Minimum Operations to Halve Array Sum
// https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

private struct MaxHeap {
    private var data: [Double] = []
    var isEmpty: Bool { data.isEmpty }
    mutating func push(_ x: Double) {
        data.append(x)
        siftUp(data.count - 1)
    }
    mutating func pop() -> Double {
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
    func halveArray(_ nums: [Int]) -> Int {
        var h = MaxHeap()
        var sum = 0.0
        for x in nums {
            h.push(Double(x))
            sum += Double(x)
        }
        let target = sum / 2
        var ans = 0
        while sum > target {
            let top = h.pop()
            let x = top / 2
            sum -= x
            h.push(x)
            ans += 1
        }
        return ans
    }
}
