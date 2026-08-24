// LeetCode 0350 - Intersection of Two Arrays II

// https://leetcode.com/problems/intersection-of-two-arrays-ii/



class Solution {

    fun intersect(nums1: IntArray, nums2: IntArray): IntArray {

        val counts = mutableMapOf<Int, Int>()

        for (num in nums1) {

            counts[num] = counts.getOrDefault(num, 0) + 1

        }



        val result = mutableListOf<Int>()

        for (num in nums2) {

            val count = counts.getOrDefault(num, 0)

            if (count > 0) {

                result.add(num)

                counts[num] = count - 1

            }

        }



        return result.toIntArray()

    }

}
