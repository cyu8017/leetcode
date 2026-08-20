// LeetCode 1997 - First Day Where You Have Been in All the Rooms
// https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/

function firstDayBeenInAllRooms(nextVisit: number[]): number {
    const MOD = 1000000007;
    const n = nextVisit.length;
    const dp = new Array(n).fill(0);
    for (let i = 1; i < n; i++) {
        dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2) % MOD;
        if (dp[i] < 0) dp[i] += MOD;
    }
    return dp[n - 1];
}
