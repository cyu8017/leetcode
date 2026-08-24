// LeetCode 0228 - Summary Ranges
// https://leetcode.com/problems/summary-ranges/

class Solution {
    fun summaryRanges(nums: IntArray): Array<String> {
        val result = mutableListOf<String>()
        var index = 0

        while (index < nums.size) {
            val start = nums[index]
            while (index + 1 < nums.size && nums[index + 1] == nums[index] + 1) {
                index++
            }
            if (start == nums[index]) {
                result.add(start.toString())
            } else {
                result.add("$start->${nums[index]}")
            }
            index++
        }

        return result.toTypedArray()
    }
}
