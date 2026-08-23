// LeetCode 2003 - Smallest Missing Genetic Value in Each Subtree
// https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/

import java.util.*;

class Solution {
    private List<Integer>[] children;
    private int[] nums;
    private Set<Integer> seen;

    public int[] smallestMissingValueSubtree(int[] parents, int[] nums) {
        this.nums = nums;
        int n = parents.length;
        children = new ArrayList[n];
        for (int i = 0; i < n; i++) children[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) children[parents[i]].add(i);
        int[] ans = new int[n];
        Arrays.fill(ans, 1);
        int one = -1;
        for (int i = 0; i < n; i++) if (nums[i] == 1) { one = i; break; }
        if (one < 0) return ans;
        seen = new HashSet<>();
        int miss = 1, node = one, prev = -1;
        while (node != -1) {
            for (int v : children[node]) if (v != prev) collect(v);
            seen.add(nums[node]);
            while (seen.contains(miss)) miss++;
            ans[node] = miss;
            prev = node;
            node = parents[node];
        }
        return ans;
    }

    private void collect(int u) {
        if (seen.contains(nums[u])) return;
        seen.add(nums[u]);
        for (int v : children[u]) collect(v);
    }
}
