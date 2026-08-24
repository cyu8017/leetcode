// LeetCode 3038 - Maximum Number of Operations With the Same Score I
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/

class Solution {
    fun maxOperations(nums: IntArray): Int {
        var s = nums[0] + nums[1]
        var n = nums.size
        var ans = 0
        run {
            var i = 0
            while (i + 1 < n && nums[i] + nums[i + 1] == s) {
                ans++
                i += 2
            }
        }
        return ans
    }
}
