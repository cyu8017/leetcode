// LeetCode 2419 - Longest Subarray With Maximum Bitwise AND
// https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution {
    fun longestSubarray(nums: IntArray): Int {
            var mx: Int = nums[0]
            for (x in nums) if (x > mx) mx = x
            var ans: Int = 0
            var cur: Int = 0
            for (x in nums) {
                if (x == mx) {
                    cur = cur + 1
                    ans = maxOf(ans, cur)
                } else {
                    cur = 0
                }
            }
            return ans
    }
}
