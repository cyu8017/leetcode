// LeetCode 0679 - 24 Game
// https://leetcode.com/problems/24-game/

class Solution {
    private val eps = 1e-6

    fun judgePoint24(cards: IntArray): Boolean {
        val nums = cards.map { it.toDouble() }.toMutableList()
        return dfs(nums)
    }

    private fun dfs(nums: MutableList<Double>): Boolean {
        if (nums.size == 1) return kotlin.math.abs(nums[0] - 24.0) < eps
        for (i in nums.indices) {
            for (j in nums.indices) {
                if (i == j) continue
                val rest = ArrayList<Double>()
                for (k in nums.indices) {
                    if (k != i && k != j) rest.add(nums[k])
                }
                val a = nums[i]
                val b = nums[j]
                val candidates = ArrayList<Double>()
                candidates.add(a + b)
                candidates.add(a - b)
                candidates.add(a * b)
                if (kotlin.math.abs(b) > eps) candidates.add(a / b)
                for (value in candidates) {
                    rest.add(value)
                    if (dfs(rest)) return true
                    rest.removeAt(rest.size - 1)
                }
            }
        }
        return false
    }
}
