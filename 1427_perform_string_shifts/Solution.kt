// LeetCode 1427 - Perform String Shifts
// https://leetcode.com/problems/perform-string-shifts/

class Solution {
    fun stringShift(s: String, shift: Array<IntArray>): String {
        var offset = 0
        for (pair in shift) {
            offset += if (pair[0] == 1) pair[1] else -pair[1]
        }
        offset %= s.length
        if (offset < 0) offset += s.length
        if (offset == 0) return s
        return s.takeLast(offset) + s.dropLast(offset)
    }
}
