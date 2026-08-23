// LeetCode 2505 - Bitwise OR of All Subsequence Sums
// https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/

class Solution {
    public long subsequenceSumOr(int[] nums) {
        long ans = 0, prefix = 0;
        for (int x : nums) {
            prefix += x;
            ans |= (long)x | prefix;
        }
        return ans;
    }
}
