// LeetCode 3702 - Longest Subsequence With Non-Zero Bitwise XOR
// https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

class Solution {
    public int longestSubsequence(int[] nums) {
        int xorv = 0, cnt0 = 0;
        for (int x : nums) {
            xorv ^= x;
            if (x == 0) cnt0++;
        }
        int n = nums.length;
        if (xorv != 0) return n;
        if (cnt0 == n) return 0;
        return n - 1;
    }
}
