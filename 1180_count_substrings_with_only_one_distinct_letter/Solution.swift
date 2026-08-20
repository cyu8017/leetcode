// LeetCode 1180 - Count Substrings with Only One Distinct Letter
// https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

class Solution {
    func countLetters(_ s: String) -> Int {
        let chars = Array(s)
        var ans = 1, length = 1
        for i in 1..<chars.count {
            length = chars[i] == chars[i - 1] ? length + 1 : 1
            ans += length
        }
        return ans
    }
}
