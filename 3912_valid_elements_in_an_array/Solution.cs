// LeetCode 3912 - Valid Elements In An Array
// https://leetcode.com/problems/valid-elements-in-an-array/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] FindValidElements(int[] nums) {
        int n = nums.Length;
        var right = new int[n];
        right[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) right[i] = Math.Max(right[i + 1], nums[i]);
        int left = 0;
        var ans = new List<int>();
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            if (x > left || i == n - 1 || x > right[i + 1]) ans.Add(x);
            left = Math.Max(left, x);
        }
        return ans.ToArray();
    }
}
