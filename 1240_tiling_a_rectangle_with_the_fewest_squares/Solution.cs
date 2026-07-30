// LeetCode 1240 - Tiling a Rectangle with the Fewest Squares
// https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

using System;
using System.Linq;

public class Solution {
    private int[] heights;
    private int rowLimit;
    private int best;

    public int TilingRectangle(int n, int m) {
        if (n > m) (n, m) = (m, n);
        rowLimit = n;
        heights = new int[m];
        best = n * m;
        Search(0);
        return best;
    }

    private void Search(int used) {
        if (used >= best) return;
        int low = heights.Min();
        if (low == rowLimit) {
            best = used;
            return;
        }
        int left = Array.IndexOf(heights, low);
        int right = left;
        while (right < heights.Length && heights[right] == low) right++;
        int maxSize = Math.Min(rowLimit - low, right - left);
        for (int size = maxSize; size >= 1; size--) {
            for (int i = left; i < left + size; i++) heights[i] = low + size;
            Search(used + 1);
            for (int i = left; i < left + size; i++) heights[i] = low;
        }
    }
}
