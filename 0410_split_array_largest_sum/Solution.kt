// LeetCode 0410 - Split Array Largest Sum

// https://leetcode.com/problems/split-array-largest-sum/



class Solution {

    fun splitArray(nums: IntArray, k: Int): Int {

        var left = nums.max()

        var right = nums.sum()



        while (left < right) {

            val mid = left + (right - left) / 2



            if (canSplit(nums, k, mid)) {

                right = mid

            } else {

                left = mid + 1

            }

        }



        return left

    }



    private fun canSplit(nums: IntArray, k: Int, limit: Int): Boolean {

        var parts = 1

        var current = 0



        for (value in nums) {

            if (current + value > limit) {

                parts++

                current = 0

            }

            current += value

        }



        return parts <= k

    }

}
