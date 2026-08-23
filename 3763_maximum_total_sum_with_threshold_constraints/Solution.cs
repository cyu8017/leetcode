// LeetCode 3763 - Maximum Total Sum With Threshold Constraints
// https://leetcode.com/problems/maximum-total-sum-with-threshold-constraints/

using System;
using System.Collections.Generic;

public class Solution {
    public long MaxSum(int[] nums, int[] threshold) {
        int n = nums.Length;
        int[] idx = new int[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Array.Sort(idx, (a, b) => threshold[a].CompareTo(threshold[b]));
        var tree = new SortedDictionary<int, int>();
        long ans = 0;
        int i2 = 0;
        for (int step = 1; ; step++) {
            while (i2 < n && threshold[idx[i2]] <= step) {
                int v = nums[idx[i2]];
                if (!tree.ContainsKey(v)) tree[v] = 0;
                tree[v]++;
                i2++;
            }
            if (tree.Count == 0) break;
            int maxKey = 0;
            foreach (var key in tree.Keys) maxKey = key;
            ans += maxKey;
            tree[maxKey]--;
            if (tree[maxKey] == 0) tree.Remove(maxKey);
        }
        return ans;
    }
}
