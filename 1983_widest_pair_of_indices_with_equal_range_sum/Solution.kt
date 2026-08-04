// LeetCode 1983
// https://leetcode.com/problems/widest-pair-of-indices-with-equal-range-sum/

class Solution {
    fun widestPairOfIndices(nums1: IntArray, nums2: IntArray): Int {
        val first = HashMap<Int, Int>()
        first[0] = -1
        var ans = 0
        var s = 0
        for (i in nums1.indices) {
            s += nums1[i] - nums2[i]
            if (s in first) ans = maxOf(ans, i - first[s]!!)
            else first[s] = i
        }
        return ans
    }
}
