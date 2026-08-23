// LeetCode 3951 - Minimum Energy To Maintain Brightness
// https://leetcode.com/problems/minimum-energy-to-maintain-brightness/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public long minEnergy(int n, int brightness, int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> merged = new ArrayList<>();
        merged.add(new int[] { intervals[0][0], intervals[0][1] });
        for (int i = 1; i < intervals.length; i++) {
            int[] x = intervals[i];
            int[] last = merged.get(merged.size() - 1);
            if (last[1] < x[0]) merged.add(new int[] { x[0], x[1] });
            else if (x[1] > last[1]) last[1] = x[1];
        }
        long ans = 0;
        for (int[] interval : merged) {
            int m = interval[1] - interval[0] + 1;
            ans += (long) ((brightness + 2) / 3) * m;
        }
        return ans;
    }
}
