// LeetCode 3496 - Maximize Score After Pair Deletions
// https://leetcode.com/problems/maximize-score-after-pair-deletions/

class Solution {
    fun maximizeScore(nums: IntArray): Int {
        var n = nums.size
        var total = 0
        for (x in nums) { total += x }
        if (n % 2 == 1) {
            var mn = nums[0]
            for (x in nums) { if (x < mn) mn = x }
            return total - mn
        }
        var mn = nums[0] + nums[1]
        run {
            var i = 0
            while (i + 1 < n) {
                mn = minOf(mn, nums[i] + nums[i + 1])
                i = i + 1
            }
        }
        return total - mn
    }
}
