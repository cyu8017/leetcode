// LeetCode 1376 - Time Needed To Inform All Employees
// https://leetcode.com/problems/time-needed-to-inform-all-employees/

using System.Collections.Generic;
public class Solution {
    public int NumOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        var children = new List<int>[n];
        for (int i = 0; i < n; i++) children[i] = new List<int>();
        for (int i = 0; i < n; i++) if (manager[i] != -1) children[manager[i]].Add(i);
        int Dfs(int u) {
            int best = 0;
            foreach (int v in children[u]) best = System.Math.Max(best, Dfs(v));
            return informTime[u] + best;
        }
        return Dfs(headID);
    }
}
