// LeetCode 3628 - Maximum Number of Subsequences After One Inserting
// https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/

class Solution {
    func calc(_ s: String, _ t: String) -> Int {
        let t0 = t.first!, t1 = t.last!
        var cnt = 0, a = 0
        for c in s {
            if c == t1 { cnt += a }
            if c == t0 { a += 1 }
        }
        return cnt
    }

    func numOfSubsequences(_ s: String) -> Int {
        var l = 0, r = 0
        for c in s where c == "T" { r += 1 }
        var ans = 0, mx = 0
        for c in s {
            if c == "T" { r -= 1 }
            if c == "C" { ans += l * r }
            if c == "L" { l += 1 }
            mx = max(mx, l * r)
        }
        mx = max(mx, max(calc(s, "LC"), calc(s, "CT")))
        return ans + mx
    }
}
