// LeetCode 1671 - Minimum Number of Removals to Make Mountain Array
// https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumMountainRemovals(int[] nums) {
        int n = nums.Length;
        int[] left = Lis(nums);
        int[] rev = (int[])nums.Clone();
        Array.Reverse(rev);
        int[] right = Lis(rev);
        Array.Reverse(right);
        int best = 0;
        for (int i = 0; i < n; i++) {
            if (left[i] > 1 && right[i] > 1)
                best = Math.Max(best, left[i] + right[i] - 1);
        }
        return n - best;
    }

    private static int[] Lis(int[] a) {
        var d = new List<int>();
        var output = new int[a.Length];
        for (int i = 0; i < a.Length; i++) {
            int x = a[i];
            int idx = d.BinarySearch(x);
            if (idx < 0) idx = ~idx;
            if (idx == d.Count) d.Add(x);
            else d[idx] = x;
            output[i] = idx + 1;
        }
        return output;
    }
}
