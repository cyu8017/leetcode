// LeetCode 0848 - Shifting Letters
// https://leetcode.com/problems/shifting-letters/

class Solution {
    fun shiftingLetters(s: String, shifts: IntArray): String {
        var arr = s.toCharArray()
        var total = 0
        for (i in arr.size - 1 downTo 0) {
            total = (total + shifts[i]) % 26
            arr[i] = (char) ((arr[i] - 'a' + total) % 26 + 'a')
        }
        return String(arr)
    }
}
