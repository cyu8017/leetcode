// LeetCode 0940 - Distinct Subsequences II
// https://leetcode.com/problems/distinct-subsequences-ii/

class Solution {
    public int distinctSubseqII(String s) {
        final int MOD = 1_000_000_007;
        long[] ends = new long[26];
        long total = 1;
        for (char ch : s.toCharArray()) {
            long prev = ends[ch - 'a'];
            ends[ch - 'a'] = total;
            total = (total - prev + ends[ch - 'a'] + MOD) % MOD;
        }
        return (int) ((total - 1 + MOD) % MOD);
    }
}
