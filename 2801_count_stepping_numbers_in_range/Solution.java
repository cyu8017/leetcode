// LeetCode 2801 - Count Stepping Numbers in Range
// https://leetcode.com/problems/count-stepping-numbers-in-range/

import java.util.Arrays;

class Solution {
    private static final int MOD = 1_000_000_007;

    public int countSteppingNumbers(String low, String high) {
        int ans = (countTo(high) - countTo(dec(low))) % MOD;
        if (ans < 0) ans += MOD;
        return ans;
    }

    private int countTo(String s) {
        int[][][][] memo = new int[85][2][11][2];
        for (int[][][] a : memo)
            for (int[][] b : a)
                for (int[] c : b) Arrays.fill(c, -1);
        return dfs(s, 0, 1, -1, 0, memo);
    }

    private int dfs(String s, int pos, int tight, int last, int started, int[][][][] memo) {
        if (pos == s.length()) return started;
        if (memo[pos][tight][last + 1][started] != -1) return memo[pos][tight][last + 1][started];
        int up = tight == 1 ? s.charAt(pos) - '0' : 9;
        long ans = 0;
        for (int d = 0; d <= up; d++) {
            int nt = (tight == 1 && d == up) ? 1 : 0;
            if (started == 0) {
                if (d == 0) ans += dfs(s, pos + 1, nt, -1, 0, memo);
                else ans += dfs(s, pos + 1, nt, d, 1, memo);
            } else if (Math.abs(d - last) == 1) {
                ans += dfs(s, pos + 1, nt, d, 1, memo);
            }
        }
        return memo[pos][tight][last + 1][started] = (int) (ans % MOD);
    }

    private String dec(String s) {
        char[] arr = s.toCharArray();
        int i = arr.length - 1;
        while (i >= 0 && arr[i] == '0') {
            arr[i] = '9';
            i--;
        }
        if (i >= 0) arr[i]--;
        int j = 0;
        while (j < arr.length - 1 && arr[j] == '0') j++;
        return new String(arr, j, arr.length - j);
    }
}
