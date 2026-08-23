// LeetCode 2152 - Minimum Number of Lines to Cover Points
// https://leetcode.com/problems/minimum-number-of-lines-to-cover-points/

import java.util.Arrays;

class Solution {
    private boolean colinear(int[] a, int[] b, int[] c) {
        return (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1]);
    }

    public int minimumLines(int[][] points) {
        int n = points.length;
        if (n <= 2) return 1;
        int inf = n;
        int[] dp = new int[1 << n];
        Arrays.fill(dp, inf);
        dp[0] = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            if (dp[mask] == inf) continue;
            int i = 0;
            while (i < n && (mask & (1 << i)) != 0) i++;
            if (i == n) continue;
            int nm = mask | (1 << i);
            dp[nm] = Math.min(dp[nm], dp[mask] + 1);
            for (int j = i + 1; j < n; j++) {
                if ((mask & (1 << j)) != 0) continue;
                nm = mask | (1 << i) | (1 << j);
                for (int k = 0; k < n; k++)
                    if ((nm & (1 << k)) == 0 && colinear(points[i], points[j], points[k]))
                        nm |= 1 << k;
                dp[nm] = Math.min(dp[nm], dp[mask] + 1);
            }
        }
        return dp[(1 << n) - 1];
    }
}
