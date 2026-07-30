// LeetCode 1436 - Destination City
// https://leetcode.com/problems/destination-city/

using System.Collections.Generic;
public class Solution {
    public string DestCity(IList<IList<string>> paths) {
        var starts = new HashSet<string>();
        foreach (var p in paths) starts.Add(p[0]);
        foreach (var p in paths) if (!starts.Contains(p[1])) return p[1];
        return "";
    }
}
