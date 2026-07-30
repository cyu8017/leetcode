// LeetCode 1981 - Minimize the Difference Between Target and Chosen Elements
// https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MinimizeTheDifference(int[][] mat, int target) {
        var possible = new HashSet<int> { 0 };
        foreach (var row in mat) {
            var uniq = new HashSet<int>(row);
            var nxt = new HashSet<int>();
            foreach (int s in possible)
                foreach (int x in uniq) nxt.Add(s + x);
            var kept = new HashSet<int>(nxt.Where(v => v <= target));
            var above = nxt.Where(v => v > target).ToList();
            if (above.Count > 0) kept.Add(above.Min());
            possible = kept.Count > 0 ? kept : new HashSet<int> { nxt.Min() };
        }
        return possible.Min(v => Math.Abs(v - target));
    }
}