// LeetCode 1183 - Maximum Number of Ones
// https://leetcode.com/problems/maximum-number-of-ones/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MaximumNumberOfOnes(int width, int height, int sideLength, int maxOnes) {
        var counts = new List<int>();
        for (int r = 0; r < sideLength; r++) {
            for (int c = 0; c < sideLength; c++) {
                int rows = (height - r + sideLength - 1) / sideLength;
                int cols = (width - c + sideLength - 1) / sideLength;
                counts.Add(rows * cols);
            }
        }
        counts.Sort((a, b) => b.CompareTo(a));
        return counts.Take(maxOnes).Sum();
    }
}
