// LeetCode 2874 - Maximum Value of an Ordered Triplet II
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

class Solution {
    fun maximumTripletValue(nums: IntArray): Long {
        var ans = 0L
        var maxI = 0L
        var maxDiff = 0L
        for (v in nums) {
            val cur = v.toLong()
            if (maxDiff * cur > ans) ans = maxDiff * cur
            if (maxI - cur > maxDiff) maxDiff = maxI - cur
            if (cur > maxI) maxI = cur
        }
        return ans
    }
}
