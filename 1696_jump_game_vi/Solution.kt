// LeetCode 1696 - Jump Game VI
// https://leetcode.com/problems/jump-game-vi/

class Solution {
    fun maxResult(nums: IntArray, k: Int): Int {
        val q = ArrayDeque<IntArray>()
        q.add(intArrayOf(0, nums[0]))
        for (i in 1 until nums.size) {
            while (q.first()[0] < i - k) q.removeFirst()
            val score = nums[i] + q.first()[1]
            while (q.isNotEmpty() && q.last()[1] <= score) q.removeLast()
            q.addLast(intArrayOf(i, score))
        }
        return q.last()[1]
    }
}
