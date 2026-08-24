// LeetCode 3462 - Maximum Sum With at Most K Elements
// https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

private struct MinHeap {
    private var a: [Int] = []
    var isEmpty: Bool { a.isEmpty }
    var count: Int { a.count }
    mutating func push(_ x: Int) {
        a.append(x)
        var i = a.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if a[p] <= a[i] { break }
            a.swapAt(p, i)
            i = p
        }
    }
    mutating func pop() -> Int {
        let r = a[0]
        let last = a.removeLast()
        if !a.isEmpty {
            a[0] = last
            var i = 0
            while true {
                var s = i
                let l = 2 * i + 1, rg = 2 * i + 2
                if l < a.count && a[l] < a[s] { s = l }
                if rg < a.count && a[rg] < a[s] { s = rg }
                if s == i { break }
                a.swapAt(i, s)
                i = s
            }
        }
        return r
    }
}

class Solution {
    func maxSum(_ grid: [[Int]], _ limits: [Int], _ k: Int) -> Int {
        var h = MinHeap()
        var sum = 0
        for i in 0..<grid.count {
            var r = grid[i].sorted()
            var lim = limits[i]
            if lim > r.count { lim = r.count }
            for j in 0..<lim {
                let val = r[r.count - 1 - j]
                h.push(val)
                sum += val
                if h.count > k { sum -= h.pop() }
            }
        }
        return sum
    }
}
