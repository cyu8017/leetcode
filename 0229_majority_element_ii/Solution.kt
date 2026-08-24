// LeetCode 0229 - Majority Element II
// https://leetcode.com/problems/majority-element-ii/

class Solution {
    fun majorityElement(nums: IntArray): List<Int> {
        var candidate1: Int? = null
        var candidate2: Int? = null
        var count1 = 0
        var count2 = 0

        for (num in nums) {
            when {
                num == candidate1 -> count1++
                num == candidate2 -> count2++
                count1 == 0 -> {
                    candidate1 = num
                    count1 = 1
                }
                count2 == 0 -> {
                    candidate2 = num
                    count2 = 1
                }
                else -> {
                    count1--
                    count2--
                }
            }
        }

        count1 = 0
        count2 = 0
        for (num in nums) {
            when (num) {
                candidate1 -> count1++
                candidate2 -> count2++
            }
        }

        val threshold = nums.size / 3
        val result = mutableListOf<Int>()
        if (count1 > threshold) {
            result.add(candidate1!!)
        }
        if (candidate2 != null && candidate2 != candidate1 && count2 > threshold) {
            result.add(candidate2!!)
        }
        return result
    }
}
