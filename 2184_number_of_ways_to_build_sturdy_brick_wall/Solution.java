// LeetCode 2184 - Number of Ways to Build Sturdy Brick Wall
// https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/

import java.util.*;

class Solution {
    private List<Integer> masks = new ArrayList<>();
    private int[] bricks;

    private void gen(int remain, int mask) {
        if (remain == 0) { masks.add(mask); return; }
        for (int b : bricks) {
            if (b <= remain) {
                int nm = mask;
                if (remain - b > 0) nm |= 1 << (remain - b);
                gen(remain - b, nm);
            }
        }
    }

    public int buildWall(int height, int width, int[] bricks) {
        final int MOD = 1_000_000_007;
        this.bricks = bricks;
        masks.clear();
        gen(width, 0);
        int m = masks.size();
        List<Integer>[] compat = new ArrayList[m];
        for (int i = 0; i < m; i++) {
            compat[i] = new ArrayList<>();
            for (int j = 0; j < m; j++)
                if ((masks.get(i) & masks.get(j)) == 0) compat[i].add(j);
        }
        int[] dp = new int[m];
        Arrays.fill(dp, 1);
        for (int h = 1; h < height; h++) {
            int[] ndp = new int[m];
            for (int i = 0; i < m; i++)
                for (int j : compat[i]) ndp[j] = (ndp[j] + dp[i]) % MOD;
            dp = ndp;
        }
        int ans = 0;
        for (int v : dp) ans = (ans + v) % MOD;
        return ans;
    }
}
