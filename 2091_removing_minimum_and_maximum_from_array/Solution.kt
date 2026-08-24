// LeetCode 2091 - Removing Minimum and Maximum From Array
// https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

class Solution {
    fun minimumDeletions(nums: IntArray): Int {
        val n = nums.size
        var mi = 0
        var ma = 0
        for (i in 0 until n) {
            if (nums[i] < nums[mi]) mi = i
            if (nums[i] > nums[ma]) ma = i
        }
        if (mi > ma) {
            val t = mi
            mi = ma
            ma = t
        }
        return minOf(ma + 1, minOf(n - mi, mi + 1 + n - ma))
    }
}
