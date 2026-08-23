// LeetCode 2827 - Number of Beautiful Integers in the Range
// https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/

import java.util.Arrays;

class Solution {
    public int numberOfBeautifulIntegers(int low, int high, int k) {
        return count(high, k) - count(low - 1, k);
    }

    private int count(int n, int k) {
        if (n < 0) return 0;
        String s = Integer.toString(n);
        int[][][][][] memo = new int[12][45][22][2][2];
        for (int[][][][] a : memo)
            for (int[][][] b : a)
                for (int[][] c : b)
                    for (int[] d : c) Arrays.fill(d, -1);
        return dfs(s, k, 0, 0, 0, 1, 0, memo);
    }

    private int dfs(String s, int k, int pos, int diff, int mod, int tight, int started, int[][][][][] memo) {
        if (pos == s.length()) return (started == 1 && diff == 0 && mod == 0) ? 1 : 0;
        if (memo[pos][diff + 20][mod][tight][started] != -1) return memo[pos][diff + 20][mod][tight][started];
        int up = tight == 1 ? s.charAt(pos) - '0' : 9;
        int ans = 0;
        for (int digit = 0; digit <= up; digit++) {
            int nt = (tight == 1 && digit == up) ? 1 : 0;
            if (started == 0) {
                if (digit == 0) ans += dfs(s, k, pos + 1, diff, mod, nt, 0, memo);
                else {
                    int nd = diff + (digit % 2 == 0 ? 1 : -1);
                    ans += dfs(s, k, pos + 1, nd, digit % k, nt, 1, memo);
                }
            } else {
                int nd = diff + (digit % 2 == 0 ? 1 : -1);
                ans += dfs(s, k, pos + 1, nd, (mod * 10 + digit) % k, nt, 1, memo);
            }
        }
        return memo[pos][diff + 20][mod][tight][started] = ans;
    }
}
