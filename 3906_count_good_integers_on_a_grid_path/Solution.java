// LeetCode 3906 - Count Good Integers On A Grid Path
// https://leetcode.com/problems/count-good-integers-on-a-grid-path/

import java.util.Arrays;

class Solution {
    private boolean[] key = new boolean[16];
    private String s = "";
    private long[][] f = new long[16][10];

    public long countGoodIntegersOnPath(long l, long r, String directions) {
        Arrays.fill(key, false);
        int row = 0, col = 0;
        key[0] = true;
        for (char c : directions.toCharArray()) {
            if (c == 'D') row++;
            else col++;
            key[row * 4 + col] = true;
        }
        return calc(r) - calc(l - 1);
    }

    private long dfs(int pos, int last, boolean lim) {
        if (pos == 16) return 1;
        if (!lim && f[pos][last] != -1) return f[pos][last];
        long res = 0;
        int start = key[pos] ? last : 0;
        int end = lim ? (s.charAt(pos) - '0') : 9;
        for (int i = start; i <= end; i++) {
            int nextLast = key[pos] ? i : last;
            res += dfs(pos + 1, nextLast, lim && (i == end));
        }
        if (!lim) f[pos][last] = res;
        return res;
    }

    private long calc(long x) {
        if (x < 0) return 0;
        String t = Long.toString(x);
        s = "0".repeat(16 - t.length()) + t;
        for (int i = 0; i < 16; i++) Arrays.fill(f[i], -1);
        return dfs(0, 0, true);
    }
}
