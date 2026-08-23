// LeetCode 2505 - Bitwise OR of All Subsequence Sums
// https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/

public class Solution {
    public long SubsequenceSumOr(int[] nums) {
        long ans = 0, prefix = 0;
        foreach (int x in nums) {
            prefix += x;
            ans |= (long)x | prefix;
        }
        return ans;
    }
}
