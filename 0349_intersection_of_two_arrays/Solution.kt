// LeetCode 0349 - Intersection of Two Arrays

// https://leetcode.com/problems/intersection-of-two-arrays/



class Solution {

    fun intersection(nums1: IntArray, nums2: IntArray): IntArray {

        val set1 = nums1.toSet()

        val set2 = nums2.toSet()

        return (set1 intersect set2).toIntArray()

    }

}
