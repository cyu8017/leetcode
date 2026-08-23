// LeetCode 0940 - Distinct Subsequences II
// https://leetcode.com/problems/distinct-subsequences-ii/

public class Solution {
    public int DistinctSubseqII(string s) {
        const int MOD = 1000000007;
        long[] ends = new long[26];
        long total = 1;
        foreach (char ch in s) {
            long prev = ends[ch - 'a'];
            ends[ch - 'a'] = total;
            total = (total - prev + ends[ch - 'a'] + MOD) % MOD;
        }
        return (int)((total - 1 + MOD) % MOD);
    }
}
