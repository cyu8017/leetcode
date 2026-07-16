// LeetCode 0047 - Permutations II
// https://leetcode.com/problems/permutations-ii/

class Solution {
    fun permuteUnique(nums: IntArray): List<List<Int>> {
        nums.sort()
        val result = mutableListOf<List<Int>>()
        val path = mutableListOf<Int>()
        val used = BooleanArray(nums.size)

        fun backtrack() {
            if (path.size == nums.size) {
                result.add(path.toList())
                return
            }

            for (i in nums.indices) {
                if (used[i]) {
                    continue
                }
                if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
                    continue
                }
                used[i] = true
                path.add(nums[i])
                backtrack()
                path.removeAt(path.lastIndex)
                used[i] = false
            }
        }

        backtrack()
        return result
    }
}
