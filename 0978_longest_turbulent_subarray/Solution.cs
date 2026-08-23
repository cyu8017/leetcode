// LeetCode 0978 - Longest Turbulent Subarray
// https://leetcode.com/problems/longest-turbulent-subarray/

using System;

public class Solution {
    public int MaxTurbulenceSize(int[] arr) {
        int ans = 1, cur = 1;
        for (int i = 1; i < arr.Length; i++) {
            if (arr[i] == arr[i - 1]) cur = 1;
            else if (i == 1 || (long)(arr[i] - arr[i - 1]) * (arr[i - 1] - arr[i - 2]) < 0) cur++;
            else cur = 2;
            ans = Math.Max(ans, cur);
        }
        return ans;
    }
}
