// LeetCode 1674 - Minimum Moves to Make Array Complementary
// https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

class Solution {
    fun minMoves(nums: IntArray, limit: Int): Int {
        val n = nums.size
        val d = IntArray(2 * limit + 2)
        for (i in 0 until n / 2) {
            val a = nums[i]
            val b = nums[n - 1 - i]
            val lo = minOf(a, b) + 1
            val hi = maxOf(a, b) + limit
            val s = a + b
            d[2] += 2
            d[lo] -= 1
            d[s] -= 1
            d[s + 1] += 1
            d[hi + 1] += 1
        }
        var ans = Int.MAX_VALUE
        var cur = 0
        for (s in 2..2 * limit) {
            cur += d[s]
            ans = minOf(ans, cur)
        }
        return ans
    }
}
