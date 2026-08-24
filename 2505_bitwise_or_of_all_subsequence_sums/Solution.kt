// LeetCode 2505 - Bitwise OR of All Subsequence Sums
// https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/

class Solution {
    fun subsequenceSumOr(nums: IntArray): Long {
            var ans: Long = 0
            var prefix: Long = 0
            for (x in nums) {
                prefix +=x
                ans |=x | prefix
            }
            return ans
    }
}
