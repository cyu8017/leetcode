// LeetCode 0324 - Wiggle Sort II

// https://leetcode.com/problems/wiggle-sort-ii/



class Solution {

    fun wiggleSort(nums: IntArray) {

        val sortedNums = nums.copyOf().sortedArray()

        var left = (nums.size - 1) / 2

        var right = nums.size - 1

        for (index in nums.indices) {

            if (index % 2 == 0) {

                nums[index] = sortedNums[left]

                left--

            } else {

                nums[index] = sortedNums[right]

                right--

            }

        }

    }

}

