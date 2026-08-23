// LeetCode 0835 - Image Overlap
// https://leetcode.com/problems/image-overlap/

using System;
using System.Collections.Generic;

public class Solution {
    public int LargestOverlap(int[][] img1, int[][] img2) {
        int n = img1.Length;
        var ones1 = new List<(int, int)>();
        var ones2 = new List<(int, int)>();
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                if (img1[i][j] != 0) ones1.Add((i, j));
                if (img2[i][j] != 0) ones2.Add((i, j));
            }
        if (ones1.Count == 0 || ones2.Count == 0) return 0;
        var shifts = new Dictionary<long, int>();
        int best = 0;
        foreach (var (x1, y1) in ones1)
            foreach (var (x2, y2) in ones2) {
                long key = ((long)(x1 - x2 + n) << 16) | (uint)(y1 - y2 + n);
                if (!shifts.ContainsKey(key)) shifts[key] = 0;
                best = Math.Max(best, ++shifts[key]);
            }
        return best;
    }
}
