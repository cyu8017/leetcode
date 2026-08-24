// LeetCode 4000 - Largest Integer With Given Digit Sum
// https://leetcode.com/problems/largest-integer-with-given-digit-sum/

class Solution {
    fun largestInteger(n: Int, s0: Int): Int {
        var s = s0
        if (n * 9 < s) return -1
        var ans = 0
        for (i in 0 until n) {
            val x = if (s < 9) s else 9
            ans = ans * 10 + x
            s -= x
        }
        return ans
    }
}
