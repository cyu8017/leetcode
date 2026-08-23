// LeetCode 3695 - Maximize Alternating Sum Using Swaps
// https://leetcode.com/problems/maximize-alternating-sum-using-swaps/

using System;
using System.Collections.Generic;

public class Solution {
    public long MaxAlternatingSum(int[] nums, int[][] swaps) {
        int n = nums.Length;
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int Find(int x) {
            if (parent[x] != x) parent[x] = Find(parent[x]);
            return parent[x];
        }
        foreach (var s in swaps) {
            int a = Find(s[0]), b = Find(s[1]);
            if (a != b) parent[a] = b;
        }
        var compVals = new Dictionary<int, List<int>>();
        var compIdx = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            int r = Find(i);
            if (!compVals.ContainsKey(r)) { compVals[r] = new List<int>(); compIdx[r] = new List<int>(); }
            compVals[r].Add(nums[i]);
            compIdx[r].Add(i);
        }
        int[] arr = new int[n];
        foreach (var kv in compVals) {
            int r = kv.Key;
            var vals = kv.Value;
            var idxs = compIdx[r];
            vals.Sort((a, b) => b.CompareTo(a));
            var even = new List<int>();
            var odd = new List<int>();
            foreach (int i in idxs) {
                if (i % 2 == 0) even.Add(i);
                else odd.Add(i);
            }
            even.Sort();
            odd.Sort();
            int ei = 0;
            foreach (int v in vals) {
                if (ei < even.Count) {
                    arr[even[ei]] = v;
                    ei++;
                } else {
                    arr[odd[ei - even.Count]] = v;
                    ei++;
                }
            }
        }
        long ans = 0;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) ans += arr[i];
            else ans -= arr[i];
        }
        return ans;
    }
}
