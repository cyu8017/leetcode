// LeetCode 0491 - Non-decreasing Subsequences
// https://leetcode.com/problems/non-decreasing-subsequences/

class Solution {
    fun findSubsequences(nums: IntArray): List<List<Int>> {
        val result = mutableSetOf<List<Int>>()
        backtrack(nums, 0, mutableListOf(), result)
        return result.sorted()
    }

    private fun backtrack(
        nums: IntArray,
        start: Int,
        path: MutableList<Int>,
        result: MutableSet<List<Int>>,
    ) {
        if (path.size >= 2) {
            result.add(path.toList())
        }
        val used = mutableSetOf<Int>()
        for (index in start until nums.size) {
            if (nums[index] in used) continue
            if (path.isNotEmpty() && nums[index] < path.last()) continue
            used.add(nums[index])
            path.add(nums[index])
            backtrack(nums, index + 1, path, result)
            path.removeAt(path.lastIndex)
        }
    }
}
