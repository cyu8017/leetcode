// LeetCode 0557 - Reverse Words in a String III
// https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution {
    func reverseWords(_ s: String) -> String {
        var chars = Array(s)
        var start = 0
        for i in 0...chars.count {
            if i == chars.count || chars[i] == " " {
                var left = start
                var right = i - 1
                while left < right {
                    chars.swapAt(left, right)
                    left += 1
                    right -= 1
                }
                start = i + 1
            }
        }
        return String(chars)
    }
}
