// LeetCode 2250 - Count Number of Rectangles Containing Each Point
// https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] CountRectangles(int[][] rectangles, int[][] points) {
        var byH = new List<int>[101];
        for (int h = 0; h <= 100; h++) byH[h] = new List<int>();
        foreach (var r in rectangles) byH[r[1]].Add(r[0]);
        for (int h = 1; h <= 100; h++) byH[h].Sort();
        int[] ans = new int[points.Length];
        for (int i = 0; i < points.Length; i++) {
            int x = points[i][0], y = points[i][1], cnt = 0;
            for (int h = y; h <= 100; h++) {
                var xs = byH[h];
                int idx = xs.BinarySearch(x);
                if (idx < 0) idx = ~idx;
                cnt += xs.Count - idx;
            }
            ans[i] = cnt;
        }
        return ans;
    }
}
