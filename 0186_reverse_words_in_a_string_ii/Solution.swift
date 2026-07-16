// LeetCode 0186 - Reverse Words in a String II
// https://leetcode.com/problems/reverse-words-in-a-string-ii/

class Solution {
    func reverseWords(_ s: inout [Character]) {
        func reverse(_ left: Int, _ right: Int) {
            var left = left
            var right = right
            while left < right {
                s.swapAt(left, right)
                left += 1
                right -= 1
            }
        }

        reverse(0, s.count - 1)
        var start = 0
        for end in 0...s.count {
            if end == s.count || s[end] == " " {
                reverse(start, end - 1)
                start = end + 1
            }
        }
    }
}