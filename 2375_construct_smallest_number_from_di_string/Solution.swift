// LeetCode 2375 - Construct Smallest Number From DI String
// https://leetcode.com/problems/construct-smallest-number-from-di-string/

class Solution {
    func smallestNumber(_ pattern: String) -> String {
        let p = Array(pattern)
        let n = p.count
        var ans = Array("123456789".prefix(n + 1))
        var i = 0
        while i < n {
            if p[i] == "I" { i += 1; continue }
            var j = i
            while j < n && p[j] == "D" { j += 1 }
            var lo = i, hi = j
            while lo < hi {
                ans.swapAt(lo, hi)
                lo += 1
                hi -= 1
            }
            i = j
        }
        return String(ans)
    }
}
