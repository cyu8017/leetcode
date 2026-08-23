// LeetCode 2053 - Kth Distinct String in an Array
// https://leetcode.com/problems/kth-distinct-string-in-an-array/

using System.Collections.Generic;

public class Solution {
    public string KthDistinct(string[] arr, int k) {
        var freq = new Dictionary<string, int>();
        foreach (var s in arr) {
            if (!freq.ContainsKey(s)) freq[s] = 0;
            freq[s]++;
        }
        foreach (var s in arr) if (freq[s] == 1 && --k == 0) return s;
        return "";
    }
}
