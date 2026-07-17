// LeetCode 1750 - Minimum Length of String After Deleting Similar Ends
// https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

class Solution {
    func minimumLength(_ s: String) -> Int {
        let chars = Array(s)
        var left = 0
        var right = chars.count - 1
        while left < right && chars[left] == chars[right] {
            let ch = chars[left]
            while left <= right && chars[left] == ch {
                left += 1
            }
            while left <= right && chars[right] == ch {
                right -= 1
            }
        }
        return right - left + 1
    }
}
