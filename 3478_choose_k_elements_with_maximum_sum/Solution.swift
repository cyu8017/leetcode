// LeetCode 3478 - Choose K Elements With Maximum Sum
// https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

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
    func findMaxSum(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> [Int] {
        let n = nums1.count
        var arr = [(Int, Int, Int)]()
        for i in 0..<n { arr.append((nums1[i], nums2[i], i)) }
        arr.sort { $0.0 < $1.0 }
        var ans = Array(repeating: 0, count: n)
        var h = MinHeap()
        var sum = 0
        var i = 0
        while i < n {
            let v = arr[i].0
            let start = i
            while i < n && arr[i].0 == v { i += 1 }
            for t in start..<i { ans[arr[t].2] = sum }
            for t in start..<i {
                h.push(arr[t].1)
                sum += arr[t].1
                if h.count > k { sum -= h.pop() }
            }
        }
        return ans
    }
}
