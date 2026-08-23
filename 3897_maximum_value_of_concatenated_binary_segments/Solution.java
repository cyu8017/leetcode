// LeetCode 3897 - Maximum Value Of Concatenated Binary Segments
// https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

import java.util.Arrays;

class Solution {
    private static final int MOD = 1000000007;

    private static int group(int[] p) {
        if (p[1] == 0) return 0;
        if (p[0] > 0) return 1;
        return 2;
    }

    public int maxValue(int[] nums1, int[] nums0) {
        int n = nums1.length;
        int[][] pairs = new int[n][2];
        int b = 0;
        for (int i = 0; i < n; i++) {
            pairs[i][0] = nums1[i];
            pairs[i][1] = nums0[i];
            b += nums1[i] + nums0[i];
        }
        Arrays.sort(pairs, (a, c) -> {
            int g1 = group(a), g2 = group(c);
            if (g1 != g2) return Integer.compare(g1, g2);
            if (g1 == 0) return Integer.compare(c[0], a[0]);
            if (g1 == 1) {
                if (a[0] != c[0]) return Integer.compare(c[0], a[0]);
                return Integer.compare(a[1], c[1]);
            }
            return Integer.compare(a[1], c[1]);
        });
        int[] p = new int[b];
        p[0] = 1;
        for (int i = 1; i < b; i++) p[i] = (int) (2L * p[i - 1] % MOD);
        int ans = 0;
        b--;
        for (int[] pr : pairs) {
            int cnt1 = pr[0], cnt0 = pr[1];
            while (cnt1 > 0) {
                ans = (ans + p[b]) % MOD;
                b--;
                cnt1--;
            }
            b -= cnt0;
        }
        return ans;
    }
}
