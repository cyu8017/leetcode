// LeetCode 1787 - Make the XOR of All Segments Equal to Zero
// https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/

import java.util.Arrays;

class Solution {
    public int minChanges(int[] nums, int k) {
        int[][] freq = new int[k][1024];
        int[] size = new int[k];
        for (int i = 0; i < nums.length; i++) {
            freq[i % k][nums[i]]++;
            size[i % k]++;
        }
        final int INF = 1000000000;
        int[] dp = new int[256];
        Arrays.fill(dp, INF);
        dp[0] = 0;
        for (int i = 0; i < k; i++) {
            int[] ndp = new int[256];
            Arrays.fill(ndp, INF);
            for (int xv = 0; xv < 256; xv++) {
                int cost = size[i] - freq[i][xv];
                for (int xo = 0; xo < 256; xo++) {
                    if (dp[xo] == INF) {
                        continue;
                    }
                    int key = xo ^ xv;
                    if (dp[xo] + cost < ndp[key]) {
                        ndp[key] = dp[xo] + cost;
                    }
                }
            }
            dp = ndp;
        }
        return dp[0];
    }
}
