// LeetCode 2003 - Smallest Missing Genetic Value in Each Subtree
// https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/

using System.Collections.Generic;

public class Solution {
    public int[] SmallestMissingValueSubtree(int[] parents, int[] nums) {
        int n = parents.Length;
        var children = new List<int>[n];
        for (int i = 0; i < n; i++) children[i] = new List<int>();
        for (int i = 1; i < n; i++) children[parents[i]].Add(i);
        int[] ans = new int[n];
        System.Array.Fill(ans, 1);
        int one = -1;
        for (int i = 0; i < n; i++) if (nums[i] == 1) { one = i; break; }
        if (one < 0) return ans;
        var seen = new HashSet<int>();
        void Collect(int u) {
            if (seen.Contains(nums[u])) return;
            seen.Add(nums[u]);
            foreach (int v in children[u]) Collect(v);
        }
        int miss = 1, node = one, prev = -1;
        while (node != -1) {
            foreach (int v in children[node]) if (v != prev) Collect(v);
            seen.Add(nums[node]);
            while (seen.Contains(miss)) miss++;
            ans[node] = miss;
            prev = node;
            node = parents[node];
        }
        return ans;
    }
}
