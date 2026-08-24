// LeetCode 2207 - Maximize Number of Subsequences in a String
// https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/

class Solution {
    func maximumSubsequenceCount(_ text: String, _ pattern: String) -> Int {
        let chars = Array(pattern)
        let a = chars[0], b = chars[1]
        func count(_ s: [Character]) -> Int {
            var ca = 0, ans = 0
            for c in s {
                if c == b { ans += ca }
                if c == a { ca += 1 }
            }
            return ans
        }
        let t = Array(text)
        return max(count([a] + t), count(t + [b]))
    }
}
