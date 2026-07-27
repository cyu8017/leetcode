// LeetCode 1680 - Concatenation of Consecutive Binary Numbers
// https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

class Solution {
    fun concatenatedBinary(n: Int): Int {
        var ans = 0L
        var bits = 0
        val mod = 1_000_000_007L
        for (x in 1..n) {
            if (x and (x - 1) == 0) bits++
            ans = ((ans shl bits) + x) % mod
        }
        return ans.toInt()
    }
}
