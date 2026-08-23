// LeetCode 3337 - Total Characters in String After Transformations II
// https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

import java.util.List;

class Solution {
    private int[][] matMul(int[][] a, int[][] b, int mod) {
        int n = a.length;
        int[][] c = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < n; k++) {
                if (a[i][k] == 0) continue;
                for (int j = 0; j < n; j++) {
                    c[i][j] = (c[i][j] + (int) ((long) a[i][k] * b[k][j] % mod)) % mod;
                }
            }
        }
        return c;
    }

    private int[][] matPow(int[][] a, int e, int mod) {
        int n = a.length;
        int[][] r = new int[n][n];
        for (int i = 0; i < n; i++) r[i][i] = 1;
        while (e > 0) {
            if ((e & 1) != 0) r = matMul(r, a, mod);
            a = matMul(a, a, mod);
            e >>= 1;
        }
        return r;
    }

    public int lengthAfterTransformations(String s, int t, List<Integer> nums) {
        final int mod = 1_000_000_007;
        int[][] mat = new int[26][26];
        for (int i = 0; i < 26; i++) {
            for (int j = 1; j <= nums.get(i); j++) mat[i][(i + j) % 26] = 1;
        }
        mat = matPow(mat, t, mod);
        int[] cnt = new int[26];
        for (char c : s.toCharArray()) cnt[c - 'a']++;
        int ans = 0;
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                ans = (ans + (int) ((long) cnt[i] * mat[i][j] % mod)) % mod;
            }
        }
        return ans;
    }
}
