// LeetCode 4006 - Count Valid Prefixes
// https://leetcode.com/problems/count-valid-prefixes/


class Solution {
    func countValidPrefixes(_ s: String) -> Int {
        var ans = 0, t = 0
        for ch in s {
            if ch == "1" { t += 1 }
            else { t -= 1 }
            if t >= -1 && t <= 1 { ans += 1 }
        }
        return ans
    }
}
