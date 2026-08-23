// LeetCode 0539 - Minimum Time Difference
// https://leetcode.com/problems/minimum-time-difference/

public class Solution {
    public int FindMinDifference(IList<string> timePoints) {
        int[] minutes = timePoints
            .Select(time => {
                string[] parts = time.Split(':');
                return int.Parse(parts[0]) * 60 + int.Parse(parts[1]);
            })
            .OrderBy(value => value)
            .ToArray();

        int best = minutes[^1] - minutes[0];
        for (int i = 1; i < minutes.Length; i++) {
            best = Math.Min(best, minutes[i] - minutes[i - 1]);
        }
        return Math.Min(best, 24 * 60 - minutes[^1] + minutes[0]);
    }
}
