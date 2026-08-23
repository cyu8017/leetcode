// LeetCode 3667 - Sort Array By Absolute Value
// https://leetcode.com/problems/sort-array-by-absolute-value/

using System;

public class Solution {
    public int[] SortByAbsoluteValue(int[] nums) {
        Array.Sort(nums, (a, b) => Math.Abs(a).CompareTo(Math.Abs(b)));
        return nums;
    }
}
