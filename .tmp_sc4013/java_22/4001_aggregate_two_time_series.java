// CONFIG class=Solution method=aggregateTimeSeries types=None
// LeetCode 4001 - Aggregate Two Time Series
// https://leetcode.com/problems/aggregate-two-time-series/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[][] aggregateTimeSeries(int[][] series1, int[][] series2) {
        int m = series1.length, n = series2.length;
        int i = 0, j = 0;
        List<int[]> ans = new ArrayList<>();
        while (i < m && j < n) {
            int t1 = series1[i][0], v1 = series1[i][1];
            int t2 = series2[j][0], v2 = series2[j][1];
            if (t1 == t2) {
                ans.add(new int[] { t1, v1 + v2 });
                i++;
                j++;
            } else if (t1 < t2) {
                ans.add(new int[] { t1, v1 + v2 });
                i++;
            } else {
                ans.add(new int[] { t2, v1 + v2 });
                j++;
            }
        }
        while (i < m) {
            ans.add(new int[] { series1[i][0], series1[i][1] });
            i++;
        }
        while (j < n) {
            ans.add(new int[] { series2[j][0], series2[j][1] });
            j++;
        }
        return ans.toArray(new int[ans.size()][]);
    }
}
