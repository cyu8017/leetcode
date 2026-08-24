// LeetCode 0696 - Count Binary Substrings
// https://leetcode.com/problems/count-binary-substrings/

class Solution {
    func countBinarySubstrings(_ s: String) -> Int {
        let chars = Array(s)
        var prev = 0, cur = 1, ans = 0
        for i in 1..<chars.count {
            if chars[i] == chars[i - 1] {
                cur += 1
            } else {
                ans += min(prev, cur)
                prev = cur
                cur = 1
            }
        }
        return ans + min(prev, cur)
    }
}
