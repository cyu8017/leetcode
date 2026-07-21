// LeetCode 1874 - Minimize Product Sum of Two Arrays
// https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

class Solution {
    fun minProductSum(nums1: IntArray, nums2: IntArray): Int {
        nums1.sort()
        nums2.sortDescending()
        var sum = 0
        for (i in nums1.indices) {
            sum += nums1[i] * nums2[i]
        }
        return sum
    }
}
