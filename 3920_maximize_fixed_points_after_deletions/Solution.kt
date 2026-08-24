// LeetCode 3920 - Maximize Fixed Points After Deletions
// https://leetcode.com/problems/maximize-fixed-points-after-deletions/

class Solution {
    fun maxFixedPoints(nums: IntArray): Int {
        var tails = ArrayList<Int>()
        for (i in 0 until nums.size) {
            if (i < nums[i]) continue
            var d = i - nums[i]
            var idx = Collections.binarySearch(tails, d)
            if (idx < 0) idx = ~idx
            if (idx == tails.size) tails.add(d)
            else tails.set(idx, d)
        }
        return tails.size
    }
}
