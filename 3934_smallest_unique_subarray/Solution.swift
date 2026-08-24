// LeetCode 3934 - Smallest Unique Subarray
// https://leetcode.com/problems/smallest-unique-subarray/


class Solution {
    func smallestUniqueSubarray(_ nums: [Int]) -> Int {
        let n = nums.count
        var sa = Array(0..<n)
        var rank = nums
        var width = 1
        while width < n {
            let w = width
            let r = rank
            sa.sort { a, b in
                if r[a] != r[b] { return r[a] < r[b] }
                let ra = a + w < n ? r[a + w] : -1
                let rb = b + w < n ? r[b + w] : -1
                return ra < rb
            }
            var next = Array(repeating: 0, count: n)
            for i in 1..<n {
                let a = sa[i - 1], b = sa[i]
                let different = rank[a] != rank[b]
                let ra = a + width < n ? rank[a + width] : -1
                let rb = b + width < n ? rank[b + width] : -1
                next[b] = (different || ra != rb) ? next[a] + 1 : next[a]
            }
            rank = next
            if rank[sa[n - 1]] == n - 1 { break }
            width <<= 1
        }
        var pos = Array(repeating: 0, count: n)
        for i in 0..<n { pos[sa[i]] = i }
        var lcp = Array(repeating: 0, count: max(0, n - 1))
        var height = 0
        for i in 0..<n {
            let p = pos[i]
            if p == n - 1 {
                height = 0
                continue
            }
            let j = sa[p + 1]
            while i + height < n && j + height < n && nums[i + height] == nums[j + height] {
                height += 1
            }
            lcp[p] = height
            if height > 0 { height -= 1 }
        }
        var ans = n
        for p in 0..<n {
            let start = sa[p]
            var need = 1
            if p > 0 && lcp[p - 1] + 1 > need { need = lcp[p - 1] + 1 }
            if p + 1 < n && lcp[p] + 1 > need { need = lcp[p] + 1 }
            if need <= n - start && need < ans { ans = need }
        }
        return ans
    }
}
