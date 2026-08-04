// LeetCode 1376 - Time Needed To Inform All Employees
// https://leetcode.com/problems/time-needed-to-inform-all-employees/

import java.util.*;

class Solution {
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        List<List<Integer>> children = new ArrayList<>();
        for (int i = 0; i < n; i++) children.add(new ArrayList<>());
        for (int i = 0; i < n; i++) if (manager[i] != -1) children.get(manager[i]).add(i);
        return dfs(headID, children, informTime);
    }

    private int dfs(int u, List<List<Integer>> children, int[] informTime) {
        int best = 0;
        for (int v : children.get(u)) best = Math.max(best, dfs(v, children, informTime));
        return informTime[u] + best;
    }
}
