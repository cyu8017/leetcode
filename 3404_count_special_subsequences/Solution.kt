// LeetCode 3404 - Count Special Subsequences
// https://leetcode.com/problems/count-special-subsequences/

class Solution {
    fun numberOfSubsequences(nums: IntArray): Long {
        var n = nums.size
        var ans = 0
        for (i in 0 until n) {
            for (j in i + 2 until n) {
                for (k in j + 2 until n) {
                    for (l in k + 2 until n) {
                        if (nums[i] * nums[k] == nums[j] * nums[l]) ans++
                    }
                }
            }
        }
        return ans
    }
}
