// LeetCode 4001 - Aggregate Two Time Series
// https://leetcode.com/problems/aggregate-two-time-series/

using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> AggregateTimeSeries(int[][] series1, int[][] series2) {
        int m = series1.Length, n = series2.Length;
        int i = 0, j = 0;
        var ans = new List<IList<int>>();
        while (i < m && j < n) {
            int t1 = series1[i][0], v1 = series1[i][1];
            int t2 = series2[j][0], v2 = series2[j][1];
            if (t1 == t2) {
                ans.Add(new List<int> { t1, v1 + v2 });
                i++; j++;
            } else if (t1 < t2) {
                ans.Add(new List<int> { t1, v1 + v2 });
                i++;
            } else {
                ans.Add(new List<int> { t2, v1 + v2 });
                j++;
            }
        }
        while (i < m) { ans.Add(new List<int> { series1[i][0], series1[i][1] }); i++; }
        while (j < n) { ans.Add(new List<int> { series2[j][0], series2[j][1] }); j++; }
        return ans;
    }
}
