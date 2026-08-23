// LeetCode 2755 - Deep Merge of Two Objects
// https://leetcode.com/problems/deep-merge-of-two-objects/
// JS-only problem; simplified string-map merge stand-in.

using System.Collections.Generic;

public class Solution {
    public Dictionary<string, string> DeepMerge(Dictionary<string, string> obj1, Dictionary<string, string> obj2) {
        var output = new Dictionary<string, string>(obj1);
        foreach (var kv in obj2) output[kv.Key] = kv.Value;
        return output;
    }
}
