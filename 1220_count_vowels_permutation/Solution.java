// LeetCode 1220 - Count Vowels Permutation
// https://leetcode.com/problems/count-vowels-permutation/

class Solution {
    public int countVowelPermutation(int n) {
        final int MOD = 1_000_000_007;
        long a = 1;
        long e = 1;
        long i = 1;
        long o = 1;
        long u = 1;
        for (int t = 0; t < n - 1; t++) {
            long na = (e + i + u) % MOD;
            long ne = (a + i) % MOD;
            long ni = (e + o) % MOD;
            long no = i;
            long nu = (i + o) % MOD;
            a = na;
            e = ne;
            i = ni;
            o = no;
            u = nu;
        }
        return (int) ((a + e + i + o + u) % MOD);
    }
}
