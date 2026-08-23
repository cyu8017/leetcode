// LeetCode 3699 - Number of ZigZag Arrays I
// https://leetcode.com/problems/number-of-zigzag-arrays-i/

public class Solution {
    public int ZigZagArrays(int n, int l, int r) {
        const int MOD = 1000000007;
        int m = r - l + 1;
        if (n == 1) return m % MOD;
        int[] up = new int[m], down = new int[m];
        for (int j = 0; j < m; j++) { up[j] = 1; down[j] = 1; }
        for (int len_ = 2; len_ <= n; len_++) {
            int[] prefDown = new int[m + 1];
            for (int j = 0; j < m; j++) prefDown[j + 1] = (prefDown[j] + down[j]) % MOD;
            int[] nup = new int[m];
            for (int j = 0; j < m; j++) nup[j] = prefDown[j];
            int[] sufUp = new int[m + 1];
            for (int j = m - 1; j >= 0; j--) sufUp[j] = (sufUp[j + 1] + up[j]) % MOD;
            int[] ndown = new int[m];
            for (int j = 0; j < m; j++) ndown[j] = sufUp[j + 1];
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
