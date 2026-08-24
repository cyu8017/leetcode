// LeetCode 3362 - Zero Array Transformation III
// https://leetcode.com/problems/zero-array-transformation-iii/

private struct MaxHeap {
    private var a: [Int] = []
    var isEmpty: Bool { a.isEmpty }
    var peek: Int { a[0] }
    mutating func push(_ x: Int) {
        a.append(x)
        var i = a.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if a[p] >= a[i] { break }
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
                if l < a.count && a[l] > a[s] { s = l }
                if rg < a.count && a[rg] > a[s] { s = rg }
                if s == i { break }
                a.swapAt(i, s)
                i = s
            }
        }
        return r
    }
}

class Solution {
    func maxRemoval(_ nums: [Int], _ queries: [[Int]]) -> Int {
        let queries = queries.sorted { $0[0] < $1[0] }
        var h = MaxHeap()
        let n = nums.count
        var diff = Array(repeating: 0, count: n + 1)
        var j = 0, used = 0, cur = 0
        for i in 0..<n {
            cur += diff[i]
            while j < queries.count && queries[j][0] == i {
                h.push(queries[j][1])
                j += 1
            }
            while cur < nums[i] {
                if h.isEmpty || h.peek < i { return -1 }
                let r = h.pop()
                cur += 1
                diff[r + 1] -= 1
                used += 1
            }
        }
        return queries.count - used
    }
}
