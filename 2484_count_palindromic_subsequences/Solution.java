// LeetCode 2484 - Count Palindromic Subsequences
// https://leetcode.com/problems/count-palindromic-subsequences/

import java.util.Arrays;

class Solution {
    public int countPalindromes(String s) {
        final int mod = 1000000007;
        int n = s.length();
        int[][][] pref = new int[n][10][10];
        int[][][] suf = new int[n][10][10];
        int[] cnt = new int[10];
        for (int i = 0; i < n; i++) {
            if (i > 0) {
                for (int a = 0; a < 10; a++)
                    System.arraycopy(pref[i - 1][a], 0, pref[i][a], 0, 10);
            }
            int d = s.charAt(i) - '0';
            for (int a = 0; a < 10; a++) pref[i][a][d] += cnt[a];
            cnt[d]++;
        }
        Arrays.fill(cnt, 0);
        for (int i = n - 1; i >= 0; i--) {
            if (i + 1 < n) {
                for (int a = 0; a < 10; a++)
                    System.arraycopy(suf[i + 1][a], 0, suf[i][a], 0, 10);
            }
            int d = s.charAt(i) - '0';
            for (int a = 0; a < 10; a++) suf[i][a][d] += cnt[a];
            cnt[d]++;
        }
        int ans = 0;
        for (int i = 2; i < n - 2; i++) {
            for (int a = 0; a < 10; a++) {
                for (int b = 0; b < 10; b++) {
                    ans = (int) ((ans + (long) pref[i - 1][a][b] * suf[i + 1][a][b]) % mod);
                }
            }
        }
        return ans;
    }
}
