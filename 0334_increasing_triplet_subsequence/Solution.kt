// LeetCode 0334 - Increasing Triplet Subsequence

// https://leetcode.com/problems/increasing-triplet-subsequence/



class Solution {

    fun increasingTriplet(nums: IntArray): Boolean {

        var first = Int.MAX_VALUE

        var second = Int.MAX_VALUE

        for (num in nums) {

            when {

                num <= first -> first = num

                num <= second -> second = num

                else -> return true

            }

        }

        return false

    }

}
