// LeetCode 2418 - Sort the People
// https://leetcode.com/problems/sort-the-people/

using System;

public class Solution {
    public string[] SortPeople(string[] names, int[] heights) {
        int n = names.Length;
        int[] idx = new int[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Array.Sort(idx, (a, b) => heights[b].CompareTo(heights[a]));
        string[] ans = new string[n];
        for (int i = 0; i < n; i++) ans[i] = names[idx[i]];
        return ans;
    }
}
