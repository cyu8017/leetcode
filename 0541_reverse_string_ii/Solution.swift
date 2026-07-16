// LeetCode 0541 - Reverse String II
// https://leetcode.com/problems/reverse-string-ii/

class Solution {
    func reverseStr(_ s: String, _ k: Int) -> String {
        var chars = Array(s)
        var start = 0
        while start < chars.count {
            var left = start
            var right = min(start + k, chars.count) - 1
            while left < right {
                chars.swapAt(left, right)
                left += 1
                right -= 1
            }
            start += 2 * k
        }
        return String(chars)
    }
}
