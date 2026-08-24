// LeetCode 3282 - Reach End of Array With Max Score
// https://leetcode.com/problems/reach-end-of-array-with-max-score/

class Solution {
    fun findMaximumScore(nums: IntArray): Long {
        var ans = 0
        var maxV = 0
        for (i in 0 until nums.size - 1) {
            if (nums[i] > maxV) maxV = nums[i]
            ans += maxV
        }
        return ans
    }
}
