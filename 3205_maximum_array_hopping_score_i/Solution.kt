// LeetCode 3205 - Maximum Array Hopping Score I
// https://leetcode.com/problems/maximum-array-hopping-score-i/

class Solution {
    private var nums: IntArray? = null
    private var f: IntArray? = null
    private var n: Int = 0

    fun maxScore(nums: IntArray): Int {
        this.nums = nums
        n = nums.size
        f = IntArray(n)
        return dfs(0)
    }

    private fun dfs(i: Int): Int {
        if (f[i] > 0) {
            return f[i]
        }
        for (j in i + 1 until n) {
            f[i] = maxOf(f[i], (j - i) * nums[j] + dfs(j))
        }
        return f[i]
    }
}
