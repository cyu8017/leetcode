// LeetCode 1220 - Count Vowels Permutation
// https://leetcode.com/problems/count-vowels-permutation/

public class Solution {
    private const int Mod = 1_000_000_007;

    public int CountVowelPermutation(int n) {
        long a = 1, e = 1, i = 1, o = 1, u = 1;
        for (int t = 0; t < n - 1; t++) {
            long na = (e + i + u) % Mod;
            long ne = (a + i) % Mod;
            long ni = (e + o) % Mod;
            long no = i;
            long nu = (i + o) % Mod;
            a = na; e = ne; i = ni; o = no; u = nu;
        }
        return (int)((a + e + i + o + u) % Mod);
    }
}
