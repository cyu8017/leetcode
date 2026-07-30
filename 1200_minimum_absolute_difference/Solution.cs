// LeetCode 1200 - Minimum Absolute Difference
// https://leetcode.com/problems/minimum-absolute-difference/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<IList<int>> MinimumAbsDifference(int[] arr) {
        Array.Sort(arr);
        int best = int.MaxValue;
        for (int i = 0; i < arr.Length - 1; i++) {
            best = Math.Min(best, arr[i + 1] - arr[i]);
        }
        var ans = new List<IList<int>>();
        for (int i = 0; i < arr.Length - 1; i++) {
            if (arr[i + 1] - arr[i] == best) ans.Add(new List<int> { arr[i], arr[i + 1] });
        }
        return ans;
    }
}
