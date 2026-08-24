// LeetCode 2587 - Rearrange Array to Maximize Prefix Score
// https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

class Solution {
    fun maxScore(nums: IntArray): Int {
        nums.sort()
        var sum = 0
        var ans = 0
        for (i in nums.size - 1 downTo 0) {
            sum += nums[i]
            if (sum > 0) { ans = ans + 1 }
            else break
        }
        return ans
    }
}
