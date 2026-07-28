// LeetCode 1029 - Two City Scheduling
// https://leetcode.com/problems/two-city-scheduling/

using System;
using System.Linq;

public class Solution {
    public int TwoCitySchedCost(int[][] costs) {
        Array.Sort(costs, (a, b) => (a[0] - a[1]).CompareTo(b[0] - b[1]));
        int n = costs.Length / 2, ans = 0;
        for (int i = 0; i < n; i++) ans += costs[i][0];
        for (int i = n; i < costs.Length; i++) ans += costs[i][1];
        return ans;
    }
}
