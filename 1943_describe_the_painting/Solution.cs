// LeetCode 1943 - Describe the Painting
// https://leetcode.com/problems/describe-the-painting/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<IList<long>> SplitPainting(int[][] segments) {
        var diff = new SortedDictionary<int, long>();
        foreach (var seg in segments) {
            if (!diff.ContainsKey(seg[0])) diff[seg[0]] = 0;
            if (!diff.ContainsKey(seg[1])) diff[seg[1]] = 0;
            diff[seg[0]] += seg[2];
            diff[seg[1]] -= seg[2];
        }
        var points = diff.Keys.ToList();
        var ans = new List<IList<long>>();
        long cur = 0;
        for (int i = 0; i < points.Count - 1; i++) {
            cur += diff[points[i]];
            if (cur != 0) ans.Add(new List<long> { points[i], points[i + 1], cur });
        }
        return ans;
    }
}