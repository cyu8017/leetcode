// LeetCode 3877 - Minimum Removals To Achieve Target Xor
// https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

import java.util.Arrays;

class Solution {
    public int minRemovals(int[] nums, int target) {
        int mx = 0;
        for (int x : nums) mx = Math.max(mx, x);
        int m = 0;
        if (mx > 0) {
            int u = (int)mx;
            while (u != 0) { m++; u >>= 1; }
        }
        if ((1 << m) <= target) return -1;
        int n = nums.length;
        int N = 1 << m;
        var f = new int[n + 1][];
        for (int i = 0; i <= n; i++) {
            f[i] = new int[N];
            Arrays.fill(f[i], Integer.MIN_VALUE);
        }
        f[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            int x = nums[i - 1];
            for (int j = 0; j < N; j++) {
                f[i][j] = f[i - 1][j];
                if (f[i - 1][j ^ x] != Integer.MIN_VALUE) {
                    f[i][j] = Math.max(f[i][j], f[i - 1][j ^ x] + 1);
                }
            }
        }
        if (f[n][target] < 0) return -1;
        return n - f[n][target];
    }
}
