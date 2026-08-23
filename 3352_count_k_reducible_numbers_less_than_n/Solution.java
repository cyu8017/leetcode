// LeetCode 3352 - Count K-Reducible Numbers Less Than N
// https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private static int bitsPop(int x) {
        int c = 0;
        while (x > 0) { c += x & 1; x >>= 1; }
        return c;
    }

    private int[] red;
    private String s;
    private int k;
    private Map<Long, Integer> memo;
    private final int mod = 1_000_000_007;

    private long key(int pos, int tight, int ones) {
        return ((long) pos << 32) | ((long) tight << 16) | ones;
    }

    private int dfs(int pos, boolean tight, int ones) {
        if (pos == s.length()) {
            if (ones == 0) return 0;
            return red[ones] <= k - 1 ? 1 : 0;
        }
        long ky = key(pos, tight ? 1 : 0, ones);
        if (memo.containsKey(ky)) return memo.get(ky);
        int up = tight ? (s.charAt(pos) - '0') : 1;
        int ans = 0;
        for (int d = 0; d <= up; d++) {
            boolean nt = tight && d == up;
            ans = (ans + dfs(pos + 1, nt, ones + d)) % mod;
        }
        memo.put(ky, ans);
        return ans;
    }

    public int countKReducibleNumbers(String s, int k) {
        this.s = s;
        this.k = k;
        red = new int[801];
        red[1] = 0;
        for (int i = 2; i <= 800; i++) red[i] = 1 + red[bitsPop(i)];
        memo = new HashMap<>();
        return dfs(0, true, 0);
    }
}
