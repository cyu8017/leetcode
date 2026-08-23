// LeetCode 3551 - Minimum Swaps to Sort by Digit Sum
// https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/

using System;
using System.Collections.Generic;

public class Solution {
    int F(int x) {
        int s = 0;
        while (x != 0) { s += x % 10; x /= 10; }
        return s;
    }
    public int MinSwaps(int[] nums) {
        int n = nums.Length;
        var arr = new (int ds, int val)[n];
        for (int i = 0; i < n; i++) arr[i] = (F(nums[i]), nums[i]);
        Array.Sort(arr, (a, b) => {
            if (a.ds != b.ds) return a.ds.CompareTo(b.ds);
            return a.val.CompareTo(b.val);
        });
        var d = new Dictionary<int, int>();
        for (int i = 0; i < n; i++) d[arr[i].val] = i;
        bool[] vis = new bool[n];
        int ans = n;
        for (int i = 0; i < n; i++) {
            if (!vis[i]) {
                ans--;
                int j = i;
                while (!vis[j]) {
                    vis[j] = true;
                    j = d[nums[j]];
                }
            }
        }
        return ans;
    }
}
