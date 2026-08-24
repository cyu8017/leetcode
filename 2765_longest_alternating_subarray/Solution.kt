// LeetCode 2765 - Longest Alternating Subarray
// https://leetcode.com/problems/longest-alternating-subarray/

class Solution {
    fun alternatingSubarray(nums: IntArray): Int {
        var ans = -1
        var n = nums.size
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                var expect = if (((j - i) % 2 == 0)) -1 else 1
                if (nums[j] - nums[j - 1] != expect) break
                if (nums[i + 1] - nums[i] != 1) break
                ans = maxOf(ans, j - i + 1)
            }
        }
        return ans
    }
}
