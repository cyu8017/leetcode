// LeetCode 2631 - Group By
// https://leetcode.com/problems/group-by/

// JavaScript problem; C# stand-in.
using System;
using System.Collections.Generic;

public class Solution {
    public Dictionary<string, List<int>> GroupBy(int[] arr, Func<int, string> fn) {
        var outMap = new Dictionary<string, List<int>>();
        foreach (int x in arr) {
            string k = fn(x);
            if (!outMap.ContainsKey(k)) outMap[k] = new List<int>();
            outMap[k].Add(x);
        }
        return outMap;
    }
}
