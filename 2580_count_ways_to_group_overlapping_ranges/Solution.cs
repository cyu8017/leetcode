// LeetCode 2580 - Count Ways to Group Overlapping Ranges
// https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

using System;

public class Solution {
    public int CountWays(int[][] ranges) {
        const int MOD = 1000000007;
        Array.Sort(ranges, (a, b) => a[0].CompareTo(b[0]));
        int groups = 0, end = -1;
        foreach (var r in ranges) {
            if (r[0] > end) {
                groups++;
                end = r[1];
            } else if (r[1] > end) {
                end = r[1];
            }
        }
        int ans = 1;
        for (int i = 0; i < groups; ++i) ans = ans * 2 % MOD;
        return ans;
    }
}
