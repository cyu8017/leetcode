// LeetCode 1569 - Number of Ways to Reorder Array to Get Same BST
// https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

class Solution {
    private val mod = 1_000_000_007
    private lateinit var choose: Array<IntArray>

    fun numOfWays(nums: IntArray): Int {
        val n = nums.size
        choose = Array(n + 1) { IntArray(n + 1) }
        for (i in 0..n) {
            choose[i][0] = 1
            choose[i][i] = 1
            for (j in 1 until i) {
                choose[i][j] = (choose[i - 1][j - 1] + choose[i - 1][j]) % mod
            }
        }
        return (ways(nums) - 1 + mod) % mod
    }

    private fun ways(values: IntArray): Int {
        if (values.size < 3) return 1
        val left = mutableListOf<Int>()
        val right = mutableListOf<Int>()
        for (i in 1 until values.size) {
            if (values[i] < values[0]) left.add(values[i]) else right.add(values[i])
        }
        var result = choose[values.size - 1][left.size].toLong()
        result = result * ways(left.toIntArray()) % mod
        result = result * ways(right.toIntArray()) % mod
        return result.toInt()
    }
}
