// LeetCode 3346 - Maximum Frequency of an Element After Performing Operations I
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxFrequency(int[] nums, int k, int numOperations) {
        Array.Sort(nums);
        int n = nums.Length;
        var freq = new Dictionary<int, int>();
        foreach (int x in nums) {
            if (!freq.ContainsKey(x)) freq[x] = 0;
            freq[x]++;
        }
        int ans = 1;
        foreach (var kv in freq) {
            int t = kv.Key, f = kv.Value;
            int lo = LowerBound(nums, t - k);
            int hi = UpperBound(nums, t + k);
            int can = hi - lo;
            int use = can;
            if (use > f + numOperations) use = f + numOperations;
            if (use > ans) ans = use;
        }
        int l = 0;
        for (int r = 0; r < n; r++) {
            while (nums[r] - nums[l] > 2 * k) l++;
            int window = r - l + 1;
            if (window > numOperations) window = numOperations;
            if (window > ans) ans = window;
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
