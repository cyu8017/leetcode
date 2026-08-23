// LeetCode 2200 - Find All K-Distant Indices in an Array
// https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

using System;
using System.Collections.Generic;

public class Solution {
    public IList<int> FindKDistantIndices(int[] nums, int key, int k) {
        int n = nums.Length;
        bool[] mark = new bool[n];
        for (int i = 0; i < n; i++) {
            if (nums[i] == key) {
                int l = Math.Max(0, i - k), r = Math.Min(n - 1, i + k);
                for (int j = l; j <= r; j++) mark[j] = true;
            }
        }
        var ans = new List<int>();
        for (int i = 0; i < n; i++) if (mark[i]) ans.Add(i);
        return ans;
    }
}
