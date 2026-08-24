// LeetCode 2542 - Maximum Subsequence Score
// https://leetcode.com/problems/maximum-subsequence-score/

class Solution {
    func maxScore(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> Int {
        let n = nums1.count
        var idx = Array(0..<n)
        idx.sort { nums2[$0] > nums2[$1] }
        var pq = Heap<Int> { $0 < $1 }
        var sum = 0, ans = 0
        for i in idx {
            pq.push(nums1[i])
            sum += nums1[i]
            if pq.count > k { sum -= pq.pop() }
            if pq.count == k { ans = max(ans, sum * nums2[i]) }
        }
        return ans
    }

    private struct Heap<T> {
        var data = [T]()
        let less: (T, T) -> Bool
        init(_ less: @escaping (T, T) -> Bool) { self.less = less }
        var isEmpty: Bool { data.isEmpty }
        var count: Int { data.count }
        func peek() -> T? { data.first }
        mutating func push(_ x: T) {
            data.append(x)
            var i = data.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if !less(data[i], data[p]) { break }
                data.swapAt(i, p); i = p
            }
        }
        mutating func pop() -> T {
            let res = data[0]
            let last = data.removeLast()
            if !data.isEmpty {
                data[0] = last
                var i = 0
                while true {
                    var s = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < data.count && less(data[l], data[s]) { s = l }
                    if r < data.count && less(data[r], data[s]) { s = r }
                    if s == i { break }
                    data.swapAt(i, s); i = s
                }
            }
            return res
        }
    }

}
