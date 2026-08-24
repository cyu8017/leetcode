// LeetCode 3379 - Transformed Array
// https://leetcode.com/problems/transformed-array/

class Solution {
    fun constructTransformedArray(nums: IntArray): IntArray {
        var n = nums.size
        var ans = IntArray(n)
        for (i in 0 until n) {
            var j = ((i + nums[i]) % n + n) % n
            ans[i] = nums[j]
        }
        return ans
    }
}
