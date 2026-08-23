// LeetCode 3347 - Maximum Frequency of an Element After Performing Operations II
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxFrequency(int[] nums, int k, int numOperations) {
        Array.Sort(nums);
        var freq = new Dictionary<int, int>();
        foreach (int x in nums) {
            if (!freq.ContainsKey(x)) freq[x] = 0;
            freq[x]++;
        }
        int ans = 1;
        var candidates = new List<int>();
        var seen = new HashSet<int>();
        foreach (int x in nums) {
            foreach (int t in new int[] { x - k, x, x + k }) {
                if (seen.Add(t)) candidates.Add(t);
            }
        }
        foreach (int t in candidates) {
            int lo = LowerBound(nums, t - k);
            int hi = UpperBound(nums, t + k);
            int can = hi - lo;
            int f = freq.TryGetValue(t, out int fv) ? fv : 0;
            int use = can;
            if (use > f + numOperations) use = f + numOperations;
            if (use > ans) ans = use;
        }
        return ans;
    }

    static int LowerBound(int[] a, int x) {
        int lo = 0, hi = a.Length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < x) lo = mid + 1; else hi = mid;
        }
        return lo;
    }
    static int UpperBound(int[] a, int x) {
        int lo = 0, hi = a.Length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] <= x) lo = mid + 1; else hi = mid;
        }
        return lo;
    }
}
