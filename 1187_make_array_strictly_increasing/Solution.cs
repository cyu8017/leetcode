// LeetCode 1187 - Make Array Strictly Increasing
// https://leetcode.com/problems/make-array-strictly-increasing/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MakeArrayIncreasing(int[] arr1, int[] arr2) {
        arr2 = arr2.Distinct().OrderBy(x => x).ToArray();
        var dp = new Dictionary<int, int> { [-1] = 0 };

        foreach (int num in arr1) {
            var newDp = new Dictionary<int, int>();
            foreach (var kv in dp) {
                int prev = kv.Key, ops = kv.Value;
                if (num > prev) {
                    if (!newDp.ContainsKey(num) || newDp[num] > ops) newDp[num] = ops;
                }
                int lo = 0, hi = arr2.Length;
                while (lo < hi) {
                    int mid = (lo + hi) / 2;
                    if (arr2[mid] <= prev) lo = mid + 1;
                    else hi = mid;
                }
                if (lo < arr2.Length) {
                    int chosen = arr2[lo];
                    int nextOps = ops + 1;
                    if (!newDp.ContainsKey(chosen) || newDp[chosen] > nextOps) newDp[chosen] = nextOps;
                }
            }
            dp = newDp;
            if (dp.Count == 0) return -1;
        }
        return dp.Values.Min();
    }
}
