// LeetCode 3992 - Rearrange String to Avoid Character Pair
// https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/

class Solution {
    fun rearrangeString(s: String, x: Char, y: Char): String {
        var arr = s.toCharArray()
        var i = 0
        for (j in 0 until arr.size) {
            if (arr[j] == y) {
                var tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
                i++
            }
        }
        return String(arr)
    }
}
