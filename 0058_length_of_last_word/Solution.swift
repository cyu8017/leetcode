// LeetCode 0058 - Length of Last Word
// https://leetcode.com/problems/length-of-last-word/

class Solution {
    func lengthOfLastWord(_ s: String) -> Int {
        var length = 0
        var i = s.count - 1
        let chars = Array(s)

        while i >= 0 && chars[i] == " " {
            i -= 1
        }

        while i >= 0 && chars[i] != " " {
            length += 1
            i -= 1
        }

        return length
    }
}
