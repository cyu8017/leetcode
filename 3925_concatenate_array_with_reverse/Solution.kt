// LeetCode 3925 - Concatenate Array With Reverse
// https://leetcode.com/problems/concatenate-array-with-reverse/

class Solution {
    fun concatWithReverse(nums: IntArray): IntArray {
        val n = nums.size
        val ans = IntArray(2 * n)
        for (i in 0 until n) {
            ans[i] = nums[i]
            ans[i + n] = nums[n - i - 1]
        }
        return ans
    }
}
