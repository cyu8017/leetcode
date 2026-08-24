// LeetCode 2222 - Number of Ways to Select Buildings
// https://leetcode.com/problems/number-of-ways-to-select-buildings/

class Solution {
    func numberOfWays(_ s: String) -> Int {
        let arr = Array(s)
        var total0 = 0, total1 = 0
        for c in arr {
            if c == "0" { total0 += 1 } else { total1 += 1 }
        }
        var left0 = 0, left1 = 0, ans = 0
        for c in arr {
            if c == "0" {
                ans += left1 * (total1 - left1)
                left0 += 1
            } else {
                ans += left0 * (total0 - left0)
                left1 += 1
            }
        }
        return ans
    }
}
