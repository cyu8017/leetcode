// LeetCode 3323 - Minimize Connected Groups by Inserting Interval
// https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int minConnectedGroups(int[][] intervals, int k) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> merged = new ArrayList<>();
        for (int[] it : intervals) {
            if (merged.isEmpty() || it[0] > merged.get(merged.size() - 1)[1]) merged.add(new int[] {it[0], it[1]});
            else if (it[1] > merged.get(merged.size() - 1)[1]) merged.get(merged.size() - 1)[1] = it[1];
        }
        int m = merged.size();
        int ans = m;
        for (int i = 0; i < m; i++) {
            int end = merged.get(i)[1] + k;
            int j = i;
            while (j < m && merged.get(j)[0] <= end) j++;
            int groups = i + 1 + (m - j);
            if (groups < ans) ans = groups;
        }
        return ans;
    }
}
