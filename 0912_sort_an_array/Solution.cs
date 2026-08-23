// LeetCode 0912 - Sort an Array
// https://leetcode.com/problems/sort-an-array/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] SortArray(int[] nums) {
        if (nums.Length <= 1) return nums;
        int mid = nums.Length / 2;
        int[] left = new int[mid];
        int[] right = new int[nums.Length - mid];
        Array.Copy(nums, 0, left, 0, mid);
        Array.Copy(nums, mid, right, 0, nums.Length - mid);
        left = SortArray(left);
        right = SortArray(right);
        var merged = new List<int>(nums.Length);
        int i = 0, j = 0;
        while (i < left.Length && j < right.Length) {
            if (left[i] <= right[j]) merged.Add(left[i++]);
            else merged.Add(right[j++]);
        }
        while (i < left.Length) merged.Add(left[i++]);
        while (j < right.Length) merged.Add(right[j++]);
        return merged.ToArray();
    }
}
