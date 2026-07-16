// LeetCode 0541 - Reverse String II
// https://leetcode.com/problems/reverse-string-ii/

class Solution {
    fun reverseStr(s: String, k: Int): String {
        val chars = s.toCharArray()
        var start = 0
        while (start < chars.size) {
            var left = start
            var right = minOf(start + k, chars.size) - 1
            while (left < right) {
                val temp = chars[left]
                chars[left] = chars[right]
                chars[right] = temp
                left++
                right--
            }
            start += 2 * k
        }
        return String(chars)
    }
}
