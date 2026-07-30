// LeetCode 1997 - First Day Where You Have Been in All the Rooms
// https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/

public class Solution {
    public int FirstDayBeenInAllRooms(int[] nextVisit) {
        const int MOD = 1000000007;
        int n = nextVisit.Length;
        var dp = new long[n];
        for (int i = 1; i < n; i++)
            dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2 + MOD) % MOD;
        return (int)dp[n - 1];
    }
}