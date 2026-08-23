// LeetCode 2343 - Query Kth Smallest Trimmed Number
// https://leetcode.com/problems/query-kth-smallest-trimmed-number/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] SmallestTrimmedNumbers(string[] nums, int[][] queries) {
        int[] ans = new int[queries.Length];
        for (int qi = 0; qi < queries.Length; qi++) {
            int k = queries[qi][0], trim = queries[qi][1];
            var arr = new List<(string s, int i)>();
            for (int i = 0; i < nums.Length; i++)
                arr.Add((nums[i].Substring(nums[i].Length - trim), i));
            arr = arr.OrderBy(a => a.s).ThenBy(a => a.i).ToList();
            ans[qi] = arr[k - 1].i;
        }
        return ans;
    }
}
