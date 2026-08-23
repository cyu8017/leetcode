// LeetCode 3080 - Mark Elements on Array by Performing Queries
// https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/

using System;
using System.Collections.Generic;

public class Solution {
    public long[] UnmarkedSumArray(int[] nums, int[][] queries) {
        int n = nums.Length;
        long s = 0;
        foreach (int x in nums) s += x;
        bool[] mark = new bool[n];
        var arr = new List<(int, int)>(n);
        for (int i = 0; i < n; i++) arr.Add((nums[i], i));
        arr.Sort();
        long[] ans = new long[queries.Length];
        int j = 0;
        for (int qi = 0; qi < queries.Length; qi++) {
            int index = queries[qi][0], k = queries[qi][1];
            if (!mark[index]) {
                mark[index] = true;
                s -= nums[index];
            }
            for (; k > 0 && j < n; j++) {
                if (!mark[arr[j].Item2]) {
                    mark[arr[j].Item2] = true;
                    s -= arr[j].Item1;
                    k--;
                }
            }
            ans[qi] = s;
        }
        return ans;
    }
}
