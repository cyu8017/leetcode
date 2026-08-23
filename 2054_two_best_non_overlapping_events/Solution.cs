// LeetCode 2054 - Two Best Non-Overlapping Events
// https://leetcode.com/problems/two-best-non-overlapping-events/

using System;

public class Solution {
    public int MaxTwoEvents(int[][] events) {
        Array.Sort(events, (a, b) => a[0].CompareTo(b[0]));
        int n = events.Length;
        int[] suffix = new int[n + 1];
        for (int i = n - 1; i >= 0; i--) suffix[i] = Math.Max(suffix[i + 1], events[i][2]);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans = Math.Max(ans, events[i][2]);
            int lo = i + 1, hi = n;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (events[mid][0] > events[i][1]) hi = mid;
                else lo = mid + 1;
            }
            if (lo < n) ans = Math.Max(ans, events[i][2] + suffix[lo]);
        }
        return ans;
    }
}
