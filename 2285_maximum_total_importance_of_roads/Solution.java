// LeetCode 2285 - Maximum Total Importance of Roads
// https://leetcode.com/problems/maximum-total-importance-of-roads/

import java.util.Arrays;

class Solution {
    public long maximumImportance(int n, int[][] roads) {
        int[] deg = new int[n];
        for (var r : roads) { deg[r[0]]++; deg[r[1]]++; }
        Arrays.sort(deg);
        long ans = 0;
        for (int i = 0; i < n; i++) ans += (long)deg[i] * (i + 1);
        return ans;
    }
}
