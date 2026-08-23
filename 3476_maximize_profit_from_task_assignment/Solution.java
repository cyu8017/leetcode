// LeetCode 3476 - Maximize Profit from Task Assignment
// https://leetcode.com/problems/maximize-profit-from-task-assignment/

import java.util.Arrays;

class Solution {
    public long maxProfit(int[] workers, int[][] tasks) {
        Arrays.sort(workers);
        Arrays.sort(tasks, (a, b) -> Integer.compare(a[0], b[0]));
        long ans = 0;
        boolean[] used = new boolean[tasks.length];
        for (int w : workers) {
            int best = -1, bi = -1;
            for (int i = 0; i < tasks.length; i++) {
                if (used[i]) continue;
                if (tasks[i][0] > w) break;
                if (tasks[i][1] > best) {
                    best = tasks[i][1];
                    bi = i;
                }
            }
            if (bi >= 0) {
                used[bi] = true;
                ans += best;
            }
        }
        return ans;
    }
}
