// LeetCode 3937 - Minimum Operations To Make Array Modulo Alternating I
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/

class Solution {
    fun minOperations(nums: IntArray, k: Int): Int {
        for (i in nums.indices) nums[i] %= k
        var ans = Int.MAX_VALUE
        for (x in 0 until k) {
            for (y in 0 until k) {
                if (x == y) continue
                var cnt = 0
                for (i in nums.indices) {
                    val target = if ((i and 1) != 0) y else x
                    val diff = kotlin.math.abs(target - nums[i])
                    cnt += minOf(diff, k - diff)
                }
                ans = minOf(ans, cnt)
            }
        }
        return ans
    }
}
