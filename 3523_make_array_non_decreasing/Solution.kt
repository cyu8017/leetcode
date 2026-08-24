// LeetCode 3523 - Make Array Non-decreasing
// https://leetcode.com/problems/make-array-non-decreasing/

class Solution {
    fun maximumPossibleSize(nums: IntArray): Int {
        var ans = 0
        var mx = 0
        for (x in nums) {
            if (mx <= x) {
                ans = ans + 1
                mx = x
            }
        }
        return ans
    }
}
