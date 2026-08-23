// LeetCode 2580 - Count Ways to Group Overlapping Ranges
// https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

import java.util.Arrays;

class Solution {
    public int countWays(int[][] ranges) {
        final int MOD = 1_000_000_007;
        Arrays.sort(ranges, (a, b) -> Integer.compare(a[0], b[0]));
        int groups = 0, end = -1;
        for (int[] r : ranges) {
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
