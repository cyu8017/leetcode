// LeetCode 3032 - Count Numbers With Unique Digits II
// https://leetcode.com/problems/count-numbers-with-unique-digits-ii/

class Solution {
    private String num;
    private int[][] f;

    private void reset() {
        f = new int[num.length()][1 << 10];
        for (int i = 0; i < num.length(); i++)
            for (int j = 0; j < (1 << 10); j++) f[i][j] = -1;
    }

    private int dfs(int pos, int mask, boolean limit) {
        if (pos >= num.length()) return mask != 0 ? 1 : 0;
        if (!limit && f[pos][mask] != -1) return f[pos][mask];
        int up = limit ? num.charAt(pos) - '0' : 9;
        int ans = 0;
        for (int i = 0; i <= up; i++) {
            if (((mask >> i) & 1) != 0) continue;
            int nxt = mask | (1 << i);
            if (mask == 0 && i == 0) nxt = 0;
            ans += dfs(pos + 1, nxt, limit && i == up);
        }
        if (!limit) f[pos][mask] = ans;
        return ans;
    }

    public int numberCount(int a, int b) {
        num = Integer.toString(b);
        reset();
        int y = dfs(0, 0, true);
        num = Integer.toString(a - 1);
        reset();
        int x = dfs(0, 0, true);
        return y - x;
    }
}
