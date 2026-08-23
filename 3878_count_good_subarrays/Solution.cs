// LeetCode 3878 - Count Good Subarrays
// https://leetcode.com/problems/count-good-subarrays/

using System;
using System.Collections.Generic;

public class Solution {
    public long CountGoodSubarrays(int[] nums) {
        int n = nums.Length;
        var l = new int[n];
        Array.Fill(l, -1);
        var stk = new List<int>();
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            while (stk.Count > 0 && nums[stk[stk.Count - 1]] < x && (nums[stk[stk.Count - 1]] | x) == x) {
                stk.RemoveAt(stk.Count - 1);
            }
            if (stk.Count > 0) l[i] = stk[stk.Count - 1];
            stk.Add(i);
        }
        var r = new int[n];
        Array.Fill(r, n);
        stk.Clear();
        for (int i = n - 1; i >= 0; i--) {
            while (stk.Count > 0 && (nums[stk[stk.Count - 1]] | nums[i]) == nums[i]) {
                stk.RemoveAt(stk.Count - 1);
            }
            if (stk.Count > 0) r[i] = stk[stk.Count - 1];
            stk.Add(i);
        }
        long ans = 0;
        for (int i = 0; i < n; i++) {
            ans += (long)(i - l[i]) * (r[i] - i);
        }
        return ans;
    }
}
