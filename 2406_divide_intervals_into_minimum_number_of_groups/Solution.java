// LeetCode 2406 - Divide Intervals Into Minimum Number of Groups
// https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

import java.util.Arrays;

class Solution {
    public int minGroups(int[][] intervals) {
        int[][] events = new int[intervals.length * 2][2];
        int idx = 0;
        for (int[] it : intervals) {
            events[idx++] = new int[] {it[0], 1};
            events[idx++] = new int[] {it[1] + 1, -1};
        }
        Arrays.sort(events, (a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(a[1], b[1]);
        });
        int cur = 0, ans = 0;
        for (int[] e : events) {
            cur += e[1];
            ans = Math.max(ans, cur);
        }
        return ans;
    }
}
