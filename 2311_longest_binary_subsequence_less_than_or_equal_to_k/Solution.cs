// LeetCode 2311 - Longest Binary Subsequence Less Than or Equal to K
// https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

public class Solution {
    public int LongestSubsequence(string s, int k) {
        int zeros = 0;
        foreach (char c in s) if (c == '0') zeros++;
        long val = 0;
        int ones = 0;
        long pow = 1;
        for (int i = s.Length - 1; i >= 0; --i) {
            if (s[i] == '1') {
                if (!(pow > k || val + pow > k)) {
                    val += pow;
                    ones++;
                }
            }
            if (pow <= k) {
                if (pow > (1L << 60)) pow = k + 1;
                else pow <<= 1;
            }
        }
        return zeros + ones;
    }
}
