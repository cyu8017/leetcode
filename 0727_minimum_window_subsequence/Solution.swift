// LeetCode 0727 - Minimum Window Subsequence
// https://leetcode.com/problems/minimum-window-subsequence/

class Solution {
    func minWindow(_ s1: String, _ s2: String) -> String {
        let a = Array(s1), b = Array(s2)
        let m = a.count, n = b.count
        var best = ""
        var i = 0
        while i < m {
            var j = 0, k = i
            while k < m && j < n {
                if a[k] == b[j] { j += 1 }
                k += 1
            }
            if j < n { break }
            let end = k - 1
            j = n - 1
            k = end
            while j >= 0 {
                if a[k] == b[j] { j -= 1 }
                k -= 1
            }
            let start = k + 1
            if best.isEmpty || end - start + 1 < best.count {
                best = String(a[start...end])
            }
            i = start + 1
        }
        return best
    }
}
