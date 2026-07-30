// LeetCode 1272 - Remove Interval
// https://leetcode.com/problems/remove-interval/

using System.Collections.Generic;

public class Solution {
    public int[][] RemoveInterval(int[][] intervals, int[] toBeRemoved) {
        int left = toBeRemoved[0], right = toBeRemoved[1];
        var answer = new List<int[]>();
        foreach (var interval in intervals) {
            int start = interval[0], end = interval[1];
            if (end <= left || start >= right) {
                answer.Add(new[] { start, end });
            } else {
                if (start < left) answer.Add(new[] { start, left });
                if (end > right) answer.Add(new[] { right, end });
            }
        }
        return answer.ToArray();
    }
}
