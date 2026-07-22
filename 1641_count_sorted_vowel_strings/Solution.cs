// LeetCode 1641 - Count Sorted Vowel Strings
// https://leetcode.com/problems/count-sorted-vowel-strings/

public class Solution {
    public int CountVowelStrings(int n) {
        return (int)Comb(n + 4, 4);
    }

    private static long Comb(int n, int k) {
        if (k < 0 || k > n) return 0;
        k = System.Math.Min(k, n - k);
        long r = 1;
        for (int i = 1; i <= k; i++) r = r * (n - k + i) / i;
        return r;
    }
}
