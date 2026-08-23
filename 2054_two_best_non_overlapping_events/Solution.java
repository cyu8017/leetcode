// LeetCode 2054 - Two Best Non-Overlapping Events
// https://leetcode.com/problems/two-best-non-overlapping-events/

import java.util.*;

class Solution {
    public int maxTwoEvents(int[][] events) {
        Arrays.sort(events, (a, b) -> Integer.compare(a[0], b[0]));
        int n = events.length;
        int[] suffix = new int[n + 1];
        for (int i = n - 1; i >= 0; i--) suffix[i] = Math.max(suffix[i + 1], events[i][2]);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans = Math.max(ans, events[i][2]);
            int lo = i + 1, hi = n;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (events[mid][0] > events[i][1]) hi = mid;
                else lo = mid + 1;
            }
            if (lo < n) ans = Math.max(ans, events[i][2] + suffix[lo]);
        }
        return ans;
    }
}
