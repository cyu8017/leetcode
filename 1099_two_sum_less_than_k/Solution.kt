// LeetCode 1099 - Two Sum Less Than K
// https://leetcode.com/problems/two-sum-less-than-k/

class Solution {
    fun twoSumLessThanK(nums: IntArray, k: Int): Int {
        nums.sort()
        var lo = 0
        var hi = nums.lastIndex
        var ans = -1
        while (lo < hi) {
            val total = nums[lo] + nums[hi]
            if (total < k) {
                ans = maxOf(ans, total)
                lo++
            } else {
                hi--
            }
        }
        return ans
    }
}
