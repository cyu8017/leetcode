// LeetCode 1759 - Count Number of Homogenous Substrings
// https://leetcode.com/problems/count-number-of-homogenous-substrings/

class Solution {
    func countHomogenous(_ s: String) -> Int {
        let mod = 1_000_000_007
        let chars = Array(s.utf8)
        var ans = 0
        var i = 0
        while i < chars.count {
            var j = i
            while j < chars.count && chars[j] == chars[i] {
                j += 1
            }
            let length = j - i
            ans = (ans + length * (length + 1) / 2) % mod
            i = j
        }
        return ans
    }
}
