// LeetCode 3321 - Find X-Sum of All K-Long Subarrays II
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/

using System;
using System.Collections.Generic;

public class Solution {
    public long[] FindXSum(int[] nums, int k, int x) {
        int n = nums.Length;
        long[] ans = new long[n - k + 1];
        for (int i = 0; i <= n - k; i++) {
            var freq = new Dictionary<int, int>();
            for (int j = i; j < i + k; j++) {
                if (!freq.ContainsKey(nums[j])) freq[nums[j]] = 0;
                freq[nums[j]]++;
            }
            var arr = new List<(int v, int f)>();
            foreach (var p in freq) arr.Add((p.Key, p.Value));
            for (int a = 0; a < arr.Count; a++) {
                for (int b = a + 1; b < arr.Count; b++) {
                    if (arr[b].f > arr[a].f || (arr[b].f == arr[a].f && arr[b].v > arr[a].v)) {
                        var t = arr[a]; arr[a] = arr[b]; arr[b] = t;
                    }
                }
            }
            int lim = Math.Min(x, arr.Count);
            var keep = new HashSet<int>();
            for (int t = 0; t < lim; t++) keep.Add(arr[t].v);
            long sum = 0;
            for (int j = i; j < i + k; j++) if (keep.Contains(nums[j])) sum += nums[j];
            ans[i] = sum;
        }
        return ans;
    }
}
