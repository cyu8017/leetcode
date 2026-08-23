// LeetCode 3975 - Filter Occupied Intervals
// https://leetcode.com/problems/filter-occupied-intervals/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[][] filterOccupiedIntervals(int[][] occupiedIntervals, int freeStart, int freeEnd) {
        Arrays.sort(occupiedIntervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> busy = new ArrayList<>();
        busy.add(new int[] { occupiedIntervals[0][0], occupiedIntervals[0][1] });
        for (int i = 1; i < occupiedIntervals.length; i++) {
            int[] cur = occupiedIntervals[i];
            int[] last = busy.get(busy.size() - 1);
            if (last[1] + 1 < cur[0]) busy.add(new int[] { cur[0], cur[1] });
            else if (cur[1] > last[1]) last[1] = cur[1];
        }
        List<int[]> ans = new ArrayList<>();
        for (int[] it : busy) {
            int s = it[0], e = it[1];
            if (e < freeStart || s > freeEnd) ans.add(new int[] { s, e });
            else {
                if (s < freeStart) ans.add(new int[] { s, freeStart - 1 });
                if (e > freeEnd) ans.add(new int[] { freeEnd + 1, e });
            }
        }
        return ans.toArray(new int[ans.size()][]);
    }
}
