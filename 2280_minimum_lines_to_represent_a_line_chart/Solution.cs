// LeetCode 2280 - Minimum Lines to Represent a Line Chart
// https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

using System;

public class Solution {
    public int MinimumLines(int[][] stockPrices) {
        if (stockPrices.Length <= 1) return 0;
        Array.Sort(stockPrices, (a, b) => a[0].CompareTo(b[0]));
        int ans = 1;
        for (int i = 2; i < stockPrices.Length; i++) {
            long x0 = stockPrices[i - 2][0], y0 = stockPrices[i - 2][1];
            long x1 = stockPrices[i - 1][0], y1 = stockPrices[i - 1][1];
            long x2 = stockPrices[i][0], y2 = stockPrices[i][1];
            if ((y1 - y0) * (x2 - x1) != (y2 - y1) * (x1 - x0)) ans++;
        }
        return ans;
    }
}
