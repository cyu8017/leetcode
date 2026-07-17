// LeetCode 1751 - Maximum Number of Events That Can Be Attended II
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

import java.util.Arrays;

class Solution {
    public int maxValue(int[][] events, int k) {
        Arrays.sort(events, (a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            if (a[1] != b[1]) return Integer.compare(a[1], b[1]);
            return Integer.compare(a[2], b[2]);
        });
        int n = events.length;
        int[] starts = new int[n];
        for (int i = 0; i < n; i++) {
            starts[i] = events[i][0];
        }

        int[][] dp = new int[k + 1][n + 1];
        for (int i = n - 1; i >= 0; i--) {
            int j = upperBound(starts, events[i][1]);
            for (int remain = 1; remain <= k; remain++) {
                dp[remain][i] = Math.max(dp[remain][i + 1], events[i][2] + dp[remain - 1][j]);
            }
        }
        return dp[k][0];
    }

    private int upperBound(int[] starts, int target) {
        int lo = 0;
        int hi = starts.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (starts[mid] <= target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
