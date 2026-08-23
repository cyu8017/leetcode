// LeetCode 2484 - Count Palindromic Subsequences
// https://leetcode.com/problems/count-palindromic-subsequences/

public class Solution {
    public int CountPalindromes(string s) {
        const int mod = 1000000007;
        int n = s.Length;
        int[][][] pref = new int[n][][];
        int[][][] suf = new int[n][][];
        for (int i = 0; i < n; i++) {
            pref[i] = new int[10][];
            suf[i] = new int[10][];
            for (int a = 0; a < 10; a++) {
                pref[i][a] = new int[10];
                suf[i][a] = new int[10];
            }
        }
        int[] cnt = new int[10];
        for (int i = 0; i < n; i++) {
            if (i > 0) {
                for (int a = 0; a < 10; a++)
                    for (int b = 0; b < 10; b++)
                        pref[i][a][b] = pref[i - 1][a][b];
            }
            int d = s[i] - '0';
            for (int a = 0; a < 10; a++) pref[i][a][d] += cnt[a];
            cnt[d]++;
        }
        for (int i = 0; i < 10; i++) cnt[i] = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (i + 1 < n) {
                for (int a = 0; a < 10; a++)
                    for (int b = 0; b < 10; b++)
                        suf[i][a][b] = suf[i + 1][a][b];
            }
            int d = s[i] - '0';
            for (int a = 0; a < 10; a++) suf[i][a][d] += cnt[a];
            cnt[d]++;
        }
        int ans = 0;
        for (int i = 2; i < n - 2; i++) {
            for (int a = 0; a < 10; a++) {
                for (int b = 0; b < 10; b++) {
                    ans = (int)((ans + (long)pref[i - 1][a][b] * suf[i + 1][a][b]) % mod);
                }
            }
        }
        return ans;
    }
}
