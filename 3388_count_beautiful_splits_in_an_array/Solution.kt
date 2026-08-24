// LeetCode 3388 - Count Beautiful Splits in an Array
// https://leetcode.com/problems/count-beautiful-splits-in-an-array/

class Solution {
    private fun equal(a: IntArray, `as`: Int, ae: Int, b: IntArray, bs: Int, be: Int): Boolean {
        if (ae - as != be - bs) return false
        for (i in 0 until ae - as) { if (a[as + i] != b[bs + i]) return false }
        return true
    }

    fun beautifulSplits(nums: IntArray): Int {
        var n = nums.size
        var ans = 0
        for (i in 1 until n - 1) {
            for (j in i + 1 until n) {
                var ok = false
                if (i <= j - i && equal(nums, 0, i, nums, i, i + i)) ok = true
                if (!ok && j - i <= n - j && equal(nums, i, j, nums, j, j + (j - i))) ok = true
                if (ok) ans++
            }
        }
        return ans
    }
}
