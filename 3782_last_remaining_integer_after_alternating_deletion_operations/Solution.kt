// LeetCode 3782 - Last Remaining Integer After Alternating Deletion Operations
// https://leetcode.com/problems/last-remaining-integer-after-alternating-deletion-operations/

class Solution {
    fun lastRemaining(n0: Long): Long {
        var n = n0
        var first = 1L
        var step = 2L
        var left = true
        while (n > 1) {
            if (!left && n % 2L == 0L) first += step
            n = (n + 1) / 2
            step *= 2
            left = !left
        }
        return first
    }
}
