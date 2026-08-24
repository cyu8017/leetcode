// LeetCode 0926 - Flip String to Monotone Increasing
// https://leetcode.com/problems/flip-string-to-monotone-increasing/

class Solution {
    func minFlipsMonoIncr(_ s: String) -> Int {
        var ones = 0, ans = 0
        for ch in s {
            if ch == "1" { ones += 1 }
            else { ans = min(ans + 1, ones) }
        }
        return ans
    }
}
