// LeetCode 1375 - Number of Times Binary String Is Prefix-Aligned
// https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

class Solution {
    func numTimesAllBlue(_ flips: [Int]) -> Int {
        var ans = 0, mx = 0
        for (i, x) in flips.enumerated() {
            mx = max(mx, x)
            if mx == i + 1 { ans += 1 }
        }
        return ans
    }
}
