// LeetCode 0986 - Interval List Intersections
// https://leetcode.com/problems/interval-list-intersections/

using System;
using System.Collections.Generic;

public class Solution {
    public int[][] IntervalIntersection(int[][] firstList, int[][] secondList) {
        int i = 0, j = 0;
        var ans = new List<int[]>();
        while (i < firstList.Length && j < secondList.Length) {
            int lo = Math.Max(firstList[i][0], secondList[j][0]);
            int hi = Math.Min(firstList[i][1], secondList[j][1]);
            if (lo <= hi) ans.Add(new[] { lo, hi });
            if (firstList[i][1] < secondList[j][1]) i++;
            else j++;
        }
        return ans.ToArray();
    }
}
