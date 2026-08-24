// LeetCode 3022 - Minimize OR of Remaining Elements Using Operations
// https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/

class Solution {
    fun minOrAfterOperations(nums: IntArray, k: Int): Int {
        var ans = 0
        var rans = 0
        for (i in 29 downTo 0) {
            var test = ans + (1 shl i)
            var cnt = 0
            var `val` = 0
            for (num in nums) {
                if (val == 0) val = test & num
                else val &= test & num
                if (val != 0) cnt++
            }
            if (cnt > k) rans += (1 shl i)
            else ans += (1 shl i)
        }
        return rans
    }
}
