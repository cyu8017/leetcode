// LeetCode 3892 - Minimum Operations to Achieve At Least K Peaks
// https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

class Solution {
    private lateinit var cost: LongArray
    private val INF = 1L shl 60

    fun minOperations(nums: IntArray, k: Int): Long {
        val n = nums.size
        if (k == 0) return 0
        if (k > n / 2) return -1
        cost = LongArray(n)
        for (i in 0 until n) {
            val left = nums[(i + n - 1) % n]
            val right = nums[(i + 1) % n]
            val need = maxOf(left, right)
            if (need >= nums[i]) cost[i] = need.toLong() - nums[i] + 1
        }
        var answer = line(1, n - 1, k)
        var withFirst = line(2, n - 2, k - 1)
        if (withFirst != INF) {
            withFirst += cost[0]
            answer = minOf(answer, withFirst)
        }
        if (answer == INF) return -1
        return answer
    }

    private fun line(left: Int, right: Int, choose: Int): Long {
        if (choose == 0) return 0
        if (left > right || choose > (right - left + 2) / 2) return INF
        var prev2 = LongArray(choose + 1)
        var prev1 = LongArray(choose + 1)
        prev2.fill(INF)
        prev1.fill(INF)
        prev2[0] = 0
        prev1[0] = 0
        for (i in left..right) {
            val current = prev1.clone()
            for (j in 1..choose) {
                if (prev2[j - 1] != INF && prev2[j - 1] + cost[i] < current[j]) {
                    current[j] = prev2[j - 1] + cost[i]
                }
            }
            prev2 = prev1
            prev1 = current
        }
        return prev1[choose]
    }
}
