// LeetCode 1250 - Check If It Is a Good Array
// https://leetcode.com/problems/check-if-it-is-a-good-array/

class Solution {
    fun isGoodArray(nums: IntArray): Boolean {
        var g = nums[0]
        for (i in 1 until nums.size) g = gcd(g, nums[i])
        return g == 1
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val t = x % y
            x = y
            y = t
        }
        return kotlin.math.abs(x)
    }
}
