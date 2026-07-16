// LeetCode 0413 - Arithmetic Slices

// https://leetcode.com/problems/arithmetic-slices/



class Solution {

    fun numberOfArithmeticSlices(nums: IntArray): Int {

        if (nums.size < 3) {

            return 0

        }



        var total = 0

        var current = 0



        for (index in 2 until nums.size) {

            if (nums[index] - nums[index - 1] == nums[index - 1] - nums[index - 2]) {

                current++

                total += current

            } else {

                current = 0

            }

        }



        return total

    }

}
