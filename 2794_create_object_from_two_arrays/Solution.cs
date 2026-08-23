// LeetCode 2794 - Create Object from Two Arrays
// https://leetcode.com/problems/create-object-from-two-arrays/
// JS-only problem; C# string-map stand-in.

using System;
using System.Collections.Generic;

public class Solution {
    public Dictionary<string, int> CreateObject(string[] keysArr, int[] valuesArr) {
        var output = new Dictionary<string, int>();
        int n = Math.Min(keysArr.Length, valuesArr.Length);
        for (int i = 0; i < n; i++) {
            if (!output.ContainsKey(keysArr[i])) output[keysArr[i]] = valuesArr[i];
        }
        return output;
    }
}
