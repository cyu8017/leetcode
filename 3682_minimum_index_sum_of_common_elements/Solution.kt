// LeetCode 3682 - Minimum Index Sum of Common Elements
// https://leetcode.com/problems/minimum-index-sum-of-common-elements/

class Solution {
    fun minimumSum(nums1: IntArray, nums2: IntArray): Int {
        var inf = 1  shl  30
        var d = HashMap<Int, Int>()
        for (i in 0 until nums2.size) { d.putIfAbsent(nums2[i], i) }
        var ans = inf
        for (i in 0 until nums1.size) {
            var j = d[nums1[i]]
            if (j != null) ans = minOf(ans, i + j)
        }
        return if (ans == inf) -1 else ans
    }
}
