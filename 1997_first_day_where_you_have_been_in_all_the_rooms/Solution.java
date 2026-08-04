// LeetCode 1997 - First Day Where You Have Been in All the Rooms
// https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/

class Solution {
    public int firstDayBeenInAllRooms(int[] nextVisit) {
        final int MOD = 1_000_000_007;
        int n = nextVisit.length;
        long[] dp = new long[n];
        for (int i = 1; i < n; i++) {
            dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2) % MOD;
            if (dp[i] < 0) dp[i] += MOD;
        }
        return (int) dp[n - 1];
    }
}
