// LeetCode 1427 - Perform String Shifts
// https://leetcode.com/problems/perform-string-shifts/

class Solution {
    fun stringShift(s: String, shift: Array<IntArray>): String {
        var offset = 0
        for (pair in shift) {
            offset += if (pair[0] == 1) pair[1] else -pair[1]
        }
        val n = s.length
        offset %= n
        if (offset < 0) offset += n
        if (offset == 0) return s
        return s.substring(n - offset) + s.substring(0, n - offset)
    }
}
