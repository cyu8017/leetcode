// LeetCode 0056 - Merge Intervals
// https://leetcode.com/problems/merge-intervals/

public class Solution {
    public int[][] Merge(int[][] intervals) {
        Array.Sort(intervals, (left, right) => left[0].CompareTo(right[0]));
        var merged = new List<int[]> { intervals[0] };

        for (int i = 1; i < intervals.Length; i++) {
            var current = intervals[i];
            var last = merged[merged.Count - 1];

            if (current[0] <= last[1]) {
                last[1] = Math.Max(last[1], current[1]);
            } else {
                merged.Add(current);
            }
        }

        return merged.ToArray();
    }
}
