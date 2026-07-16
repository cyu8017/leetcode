// LeetCode 0090 - Subsets II
// https://leetcode.com/problems/subsets-ii/

class Solution {
    fun subsetsWithDup(nums: IntArray): List<List<Int>> {
        nums.sort()
        val result = mutableListOf<List<Int>>()
        val path = mutableListOf<Int>()

        fun backtrack(start: Int) {
            result.add(path.toList())
            for (i in start until nums.size) {
                if (i > start && nums[i] == nums[i - 1]) {
                    continue
                }
                path.add(nums[i])
                backtrack(i + 1)
                path.removeAt(path.size - 1)
            }
        }

        backtrack(0)
        return result
    }
}
