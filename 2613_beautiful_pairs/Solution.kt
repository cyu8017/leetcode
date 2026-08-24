// LeetCode 2613 - Beautiful Pairs
// https://leetcode.com/problems/beautiful-pairs/

class Solution {
    fun beautifulPair(nums1: IntArray, nums2: IntArray): IntArray {
        var n = nums1.size
        var best = Int.MAX_VALUE
        var ans = intArrayOf(0, 1)
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                var d = kotlin.math.abs(nums1[i] - nums1[j]) + kotlin.math.abs(nums2[i] - nums2[j])
                if (d < best || (d == best && (i < ans[0] || (i == ans[0] && j < ans[1])))) {
                    best = d
                    ans = intArrayOf(i, j)
                }
            }
        }
        return ans
    }
}
