// LeetCode 2914 - Minimum Number of Changes to Make Binary String Beautiful
// https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

class Solution {
    func minChanges(_ s: String) -> Int {
        let chars = Array(s)
        var ans = 0
        var i = 0
        while i < chars.count {
            if chars[i] != chars[i + 1] { ans += 1 }
            i += 2
        }
        return ans
    }
}
