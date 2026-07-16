// LeetCode 0396 - Rotate Function

// https://leetcode.com/problems/rotate-function/



class Solution {

    fun maxRotateFunction(nums: IntArray): Int {

        val total = nums.sum()

        var current = nums.indices.sumOf { index -> index * nums[index] }

        var best = current



        for (index in nums.size - 1 downTo 1) {

            current += total - nums.size * nums[index]

            best = maxOf(best, current)

        }



        return best

    }

}
