// LeetCode 2440 - Create Components With Same Value
// https://leetcode.com/problems/create-components-with-same-value/

using System.Collections.Generic;

public class Solution {
    private List<int>[] g;
    private int[] nums;

    public int ComponentValue(int[] nums, int[][] edges) {
        this.nums = nums;
        int n = nums.Length;
        int total = 0;
        foreach (int x in nums) total += x;
        g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        for (int parts = n; parts >= 1; parts--) {
            if (total % parts != 0) continue;
            int target = total / parts;
            if (Dfs(0, -1, target) == 0) return parts - 1;
        }
        return 0;
    }

    private int Dfs(int u, int p, int target) {
        int sum = nums[u];
        foreach (int v in g[u]) {
            if (v == p) continue;
            int sub = Dfs(v, u, target);
            if (sub < 0) return -1;
            sum += sub;
        }
        if (sum > target) return -1;
        if (sum == target) return 0;
        return sum;
    }
}
