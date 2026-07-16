// LeetCode 0344 - Reverse String
// https://leetcode.com/problems/reverse-string/

class Solution {
    func reverseString(_ s: inout [String]) {
        var left = 0
        var right = s.count - 1
        while left < right {
            s.swapAt(left, right)
            left += 1
            right -= 1
        }
    }
}
