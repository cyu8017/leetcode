// LeetCode 1029 - Two City Scheduling
// https://leetcode.com/problems/two-city-scheduling/

import java.util.Arrays;

class Solution {
    public int twoCitySchedCost(int[][] costs) {
        Arrays.sort(costs, (a, b) -> (a[0] - a[1]) - (b[0] - b[1]));
        int n = costs.length / 2, sum = 0;
        for (int i = 0; i < n; i++) sum += costs[i][0];
        for (int i = n; i < costs.length; i++) sum += costs[i][1];
        return sum;
    }
}
