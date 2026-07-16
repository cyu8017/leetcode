// LeetCode 0330 - Patching Array

// https://leetcode.com/problems/patching-array/



class Solution {

    fun minPatches(nums: IntArray, n: Int): Int {

        var patches = 0

        var miss = 1L

        var index = 0

        while (miss <= n) {

            if (index < nums.size && nums[index] <= miss) {

                miss += nums[index]

                index++

            } else {

                miss += miss

                patches++

            }

        }

        return patches

    }

}

