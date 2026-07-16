// LeetCode 0345 - Reverse Vowels of a String
// https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution {
    func reverseVowels(_ s: String) -> String {
        let vowels = Set("aeiouAEIOU")
        var chars = Array(s)
        var left = 0
        var right = chars.count - 1

        while left < right {
            while left < right && !vowels.contains(chars[left]) {
                left += 1
            }
            while left < right && !vowels.contains(chars[right]) {
                right -= 1
            }
            chars.swapAt(left, right)
            left += 1
            right -= 1
        }

        return String(chars)
    }
}
