// LeetCode 1987 - Number of Unique Good Subsequences
// https://leetcode.com/problems/number-of-unique-good-subsequences/

public class Solution {
    public int NumberOfUniqueGoodSubsequences(string binary) {
        const int MOD = 1000000007;
        long ends0 = 0, ends1 = 0;
        bool has0 = false;
        foreach (char ch in binary) {
            if (ch == '0') {
                has0 = true;
                ends0 = (ends0 + ends1) % MOD;
            } else {
                ends1 = (ends0 + ends1 + 1) % MOD;
            }
        }
        return (int)((ends0 + ends1 + (has0 ? 1 : 0)) % MOD);
    }
}