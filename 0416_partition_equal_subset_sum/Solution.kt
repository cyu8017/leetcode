// LeetCode 0416 - Partition Equal Subset Sum

// https://leetcode.com/problems/partition-equal-subset-sum/



class Solution {

    fun canPartition(nums: IntArray): Boolean {

        val total = nums.sum()



        if (total % 2 != 0) {

            return false

        }



        val target = total / 2

        var possible = mutableSetOf(0)



        for (value in nums) {

            possible = (possible + possible.mapNotNull { amount ->

                val sum = amount + value

                if (sum <= target) sum else null

            }.toSet()).toMutableSet()



            if (target in possible) {

                return true

            }

        }



        return target in possible

    }

}
