// LeetCode 2822 - Inversion of Object
// https://leetcode.com/problems/inversion-of-object/
// JS-only problem; C# string-map stand-in.

using System.Collections.Generic;

public class Solution {
    public Dictionary<string, List<string>> InvertObject(Dictionary<string, string> obj) {
        var output = new Dictionary<string, List<string>>();
        foreach (var kv in obj) {
            if (!output.ContainsKey(kv.Value)) output[kv.Value] = new List<string>();
            output[kv.Value].Add(kv.Key);
        }
        return output;
    }
}
