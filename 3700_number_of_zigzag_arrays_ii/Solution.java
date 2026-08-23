// LeetCode 3700 - Number of ZigZag Arrays II
// https://leetcode.com/problems/number-of-zigzag-arrays-ii/

class Solution {
    public int zigZagArrays(int n, int l, int r) {
        int MOD = 1000000007;
        int m = r - l + 1;
        if (n == 1) return m % MOD;
        int[] up = new int[m], down = new int[m];
        for (int j = 0; j < m; j++) { up[j] = 1; down[j] = 1; }
        for (int length = 2; length <= n; length++) {
            int[] pref = new int[m + 1];
            for (int j = 0; j < m; j++) pref[j + 1] = (pref[j] + down[j]) % MOD;
            int[] nup = new int[m];
            for (int j = 0; j < m; j++) nup[j] = pref[j];
            int[] suf = new int[m + 1];
            for (int j = m - 1; j >= 0; j--) suf[j] = (suf[j + 1] + up[j]) % MOD;
            int[] ndown = new int[m];
            for (int j = 0; j < m; j++) ndown[j] = suf[j + 1];
            up = nup;
            down = ndown;
        }
        int ans = 0;
        for (int j = 0; j < m; j++) {
            ans = (ans + up[j]) % MOD;
            ans = (ans + down[j]) % MOD;
        }
        return ans;
    }
}
