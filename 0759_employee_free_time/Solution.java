// LeetCode 0759 - Employee Free Time
// https://leetcode.com/problems/employee-free-time/

import java.util.*;

class Solution {
    public int[][] employeeFreeTime(int[][][] schedule) {
        List<int[]> intervals = new ArrayList<>();
        for (int[][] employee : schedule)
            for (int[] item : employee)
                intervals.add(new int[] {item[0], item[1]});
        intervals.sort(Comparator.comparingInt(a -> a[0]));
        List<int[]> merged = new ArrayList<>();
        for (int[] iv : intervals) {
            if (merged.isEmpty() || merged.get(merged.size() - 1)[1] < iv[0]) merged.add(iv);
            else merged.get(merged.size() - 1)[1] = Math.max(merged.get(merged.size() - 1)[1], iv[1]);
        }
        List<int[]> result = new ArrayList<>();
        for (int i = 1; i < merged.size(); i++)
            result.add(new int[] {merged.get(i - 1)[1], merged.get(i)[0]});
        return result.toArray(new int[result.size()][]);
    }
}
