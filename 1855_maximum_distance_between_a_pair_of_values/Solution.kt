// LeetCode 1855 - Maximum Distance Between a Pair of Values
// https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

class Solution {
    fun maxDistance(nums1: IntArray, nums2: IntArray): Int {
        var answer = 0
        var j = 0
        for (i in nums1.indices) {
            while (j < nums2.size && nums1[i] <= nums2[j]) {
                j++
            }
            answer = maxOf(answer, j - i - 1)
        }
        return answer
    }
}
