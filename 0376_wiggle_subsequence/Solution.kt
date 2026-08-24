// LeetCode 0376 - Wiggle Subsequence

// https://leetcode.com/problems/wiggle-subsequence/



class Solution {

    fun wiggleMaxLength(nums: IntArray): Int {

        if (nums.size < 2) {

            return nums.size

        }



        var up = 1

        var down = 1



        for (index in 1 until nums.size) {

            when {

                nums[index] > nums[index - 1] -> up = down + 1

                nums[index] < nums[index - 1] -> down = up + 1

            }

        }



        return maxOf(up, down)

    }

}
