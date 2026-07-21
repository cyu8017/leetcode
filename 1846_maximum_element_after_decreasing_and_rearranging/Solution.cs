// LeetCode 1846 - Maximum Element After Decreasing and Rearranging
// https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

using System;

public class Solution {
    public int MaximumElementAfterDecrementingAndRearranging(int[] arr) {
        Array.Sort(arr);
        arr[0] = 1;
        for (int i = 1; i < arr.Length; i++) {
            arr[i] = Math.Min(arr[i], arr[i - 1] + 1);
        }
        int best = 0;
        foreach (int v in arr) best = Math.Max(best, v);
        return best;
    }
}
