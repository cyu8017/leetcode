// LeetCode 3092 - Most Frequent IDs
// https://leetcode.com/problems/most-frequent-ids/

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
    func mostFrequentIDs(_ nums: [Int], _ freq: [Int]) -> [Int] {
        let n = nums.count
        var cnt: [Int: Int] = [:]
        var lazy: [Int: Int] = [:]
        var ans = Array(repeating: 0, count: n)
        var pq = MaxHeap()
        for i in 0..<n {
            let x = nums[i], f = freq[i]
            let old = cnt[x, default: 0]
            lazy[old, default: 0] += 1
            let neu = old + f
            cnt[x] = neu
            pq.push(neu)
            while !pq.isEmpty && lazy[pq.peek(), default: 0] > 0 {
                let top = pq.pop()
                lazy[top]! -= 1
            }
            if !pq.isEmpty { ans[i] = pq.peek() }
        }
        return ans
    }
}
