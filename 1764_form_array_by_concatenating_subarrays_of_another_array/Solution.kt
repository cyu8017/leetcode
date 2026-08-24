// LeetCode 1764 - Form Array by Concatenating Subarrays of Another Array
// https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/

class Solution {
    fun canChoose(groups: Array<IntArray>, nums: IntArray): Boolean {
        return dfs(groups, nums, 0, 0)
    }

    private fun dfs(groups: Array<IntArray>, nums: IntArray, i: Int, start: Int): Boolean {
        val n = nums.size
        if (i == groups.size) {
            return start == n
        }
        val g = groups[i]
        val m = g.size
        for (j in start..n - m) {
            if (matches(nums, j, g) && dfs(groups, nums, i + 1, j + m)) {
                return true
            }
        }
        return false
    }

    private fun matches(nums: IntArray, start: Int, g: IntArray): Boolean {
        for (t in g.indices) {
            if (nums[start + t] != g[t]) {
                return false
            }
        }
        return true
    }
}
