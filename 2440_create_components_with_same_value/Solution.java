// LeetCode 2440 - Create Components With Same Value
// https://leetcode.com/problems/create-components-with-same-value/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<Integer>[] g;
    private int[] nums;

    private int dfs(int u, int p, int target) {
        int sum = nums[u];
        for (int v : g[u]) {
            if (v == p) continue;
            int sub = dfs(v, u, target);
            if (sub < 0) return -1;
            sum += sub;
        }
        if (sum > target) return -1;
        if (sum == target) return 0;
        return sum;
    }

    public int componentValue(int[] nums, int[][] edges) {
        this.nums = nums;
        int n = nums.length;
        int total = 0;
        for (int x : nums) total += x;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        for (int parts = n; parts >= 1; parts--) {
            if (total % parts != 0) continue;
            int target = total / parts;
            if (dfs(0, -1, target) == 0) return parts - 1;
        }
        return 0;
    }
}
