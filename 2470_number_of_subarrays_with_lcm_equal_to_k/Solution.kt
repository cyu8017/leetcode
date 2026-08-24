// LeetCode 2470 - Number of Subarrays With LCM Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

class Solution {
    fun subarrayLCM(nums: IntArray, k: Int): Int {
        var ans = 0
        val n = nums.size
        for (i in 0 until n) {
            var cur = 1L
            for (j in i until n) {
                cur = cur / gcd(cur.toInt(), nums[j]) * nums[j]
                if (cur > k) break
                if (cur == k.toLong()) ans++
            }
        }
        return ans
    }

    private fun gcd(a0: Int, b0: Int): Int {
        var a = a0
        var b = b0
        while (b != 0) {
            val t = a % b
            a = b
            b = t
        }
        return a
    }
}
