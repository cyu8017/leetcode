// LeetCode 2724 - Sort By
// https://leetcode.com/problems/sort-by/

// JS sortBy stand-in
using System;

public class Solution {
    public int[] SortBy(int[] arr, Func<int, double> fn) {
        int[] outArr = (int[])arr.Clone();
        Array.Sort(outArr, (a, b) => fn(a).CompareTo(fn(b)));
        return outArr;
    }
}
