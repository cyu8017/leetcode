// LeetCode 1751 - Maximum Number of Events That Can Be Attended II
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

public class Solution {
    public int MaxValue(int[][] events, int k) {
        Array.Sort(events, (a, b) => {
            if (a[0] != b[0]) return a[0].CompareTo(b[0]);
            if (a[1] != b[1]) return a[1].CompareTo(b[1]);
            return a[2].CompareTo(b[2]);
        });
        int n = events.Length;
        int[] starts = new int[n];
        for (int i = 0; i < n; i++) {
            starts[i] = events[i][0];
        }

        int[][] dp = new int[k + 1][];
        for (int remain = 0; remain <= k; remain++) {
            dp[remain] = new int[n + 1];
        }
        for (int i = n - 1; i >= 0; i--) {
            int j = UpperBound(starts, events[i][1]);
            for (int remain = 1; remain <= k; remain++) {
                dp[remain][i] = Math.Max(dp[remain][i + 1], events[i][2] + dp[remain - 1][j]);
            }
        }
        return dp[k][0];
    }

    private int UpperBound(int[] starts, int target) {
        int lo = 0;
        int hi = starts.Length;
        while (lo < hi) {
            int mid = (lo + hi) >> 1;
            if (starts[mid] <= target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
