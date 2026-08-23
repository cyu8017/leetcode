// LeetCode 0826 - Most Profit Assigning Work
// https://leetcode.com/problems/most-profit-assigning-work/

import java.util.*;

class Solution {
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        int m = difficulty.length;
        int[][] jobs = new int[m][2];
        for (int i = 0; i < m; i++) {
            jobs[i][0] = difficulty[i];
            jobs[i][1] = profit[i];
        }
        Arrays.sort(jobs, Comparator.comparingInt(a -> a[0]));
        Arrays.sort(worker);
        int ans = 0, best = 0, i = 0;
        for (int ability : worker) {
            while (i < m && jobs[i][0] <= ability) {
                best = Math.max(best, jobs[i][1]);
                i++;
            }
            ans += best;
        }
        return ans;
    }
}
