// LeetCode 2589 - Minimum Time to Complete All Tasks
// https://leetcode.com/problems/minimum-time-to-complete-all-tasks/

import java.util.Arrays;

class Solution {
    public int findMinimumTime(int[][] tasks) {
        Arrays.sort(tasks, (a, b) -> Integer.compare(a[1], b[1]));
        boolean[] on = new boolean[2001];
        int ans = 0;
        for (int[] t : tasks) {
            int start = t[0], end = t[1], dur = t[2];
            int have = 0;
            for (int i = start; i <= end; ++i) if (on[i]) have++;
            int need = dur - have;
            for (int i = end; i >= start && need > 0; --i) {
                if (!on[i]) {
                    on[i] = true;
                    need--;
                    ans++;
                }
            }
        }
        return ans;
    }
}
