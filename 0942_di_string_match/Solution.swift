// LeetCode 0942 - DI String Match
// https://leetcode.com/problems/di-string-match/

class Solution {
    func diStringMatch(_ s: String) -> [Int] {
        var lo = 0, hi = s.count
        var ans = Array(repeating: 0, count: s.count + 1)
        var k = 0
        for ch in s {
            if ch == "I" { ans[k] = lo; lo += 1 }
            else { ans[k] = hi; hi -= 1 }
            k += 1
        }
        ans[k] = lo
        return ans
    }
}
