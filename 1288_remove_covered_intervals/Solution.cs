// LeetCode 1288 - Remove Covered Intervals
// https://leetcode.com/problems/remove-covered-intervals/

using System.Linq;

public class Solution {
    public int RemoveCoveredIntervals(int[][] intervals) {
        var sorted = intervals
            .OrderBy(x => x[0])
            .ThenByDescending(x => x[1])
            .ToArray();
        int answer = 0, farthest = -1;
        foreach (var interval in sorted) {
            if (interval[1] > farthest) {
                answer++;
                farthest = interval[1];
            }
        }
        return answer;
    }
}
