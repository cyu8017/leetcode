// LeetCode 1784 - Check if Binary String Has at Most One Segment of Ones
// https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

class Solution {
    func checkOnesSegment(_ s: String) -> Bool {
        var chars = Array(s)
        while let first = chars.first, first == "0" {
            chars.removeFirst()
        }
        while let last = chars.last, last == "0" {
            chars.removeLast()
        }
        return !String(chars).contains("01")
    }
}
