// LeetCode 3702 - Longest Subsequence With Non-Zero Bitwise XOR
// https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

public class Solution {
    public int LongestSubsequence(int[] nums) {
        int xorv = 0, cnt0 = 0;
        foreach (int x in nums) {
            xorv ^= x;
            if (x == 0) cnt0++;
        }
        int n = nums.Length;
        if (xorv != 0) return n;
        if (cnt0 == n) return 0;
        return n - 1;
    }
}
