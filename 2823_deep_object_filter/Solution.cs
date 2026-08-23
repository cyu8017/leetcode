// LeetCode 2823 - Deep Object Filter
// https://leetcode.com/problems/deep-object-filter/
// JS-only problem; C# vector filter stand-in.

using System;
using System.Collections.Generic;

public class Solution {
    public IList<int> DeepFilter(int[] obj, Func<int, bool> fn) {
        var output = new List<int>();
        foreach (int v in obj) if (fn(v)) output.Add(v);
        return output;
    }
}
