// LeetCode 2609 - Find the Longest Balanced Substring of a Binary String
// https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

class Solution {
    func findTheLongestBalancedSubstring(_ s: String) -> Int {
        var ans = 0, zeros = 0, ones = 0
        for c in s {
            if c == "0" {
                if ones > 0 { zeros = 0; ones = 0 }
                zeros += 1
            } else {
                ones += 1
                ans = max(ans, 2 * min(ones, zeros))
            }
        }
        return ans
    }
}
