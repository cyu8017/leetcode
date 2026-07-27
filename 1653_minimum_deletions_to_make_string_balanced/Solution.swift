// LeetCode 1653 - Minimum Deletions to Make String Balanced
// https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution {
    func minimumDeletions(_ s: String) -> Int {
        var b = 0, ans = 0
        for c in s {
            if c == "b" {
                b += 1
            } else {
                ans = min(ans + 1, b)
            }
        }
        return ans
    }
}
