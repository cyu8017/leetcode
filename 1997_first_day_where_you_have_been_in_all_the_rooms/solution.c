// LeetCode 1997 - First Day Where You Have Been in All the Rooms
// https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/

#include <stdlib.h>

int firstDayBeenInAllRooms(int* nextVisit, int nextVisitSize) {
    const int MOD = 1000000007;
    int n = nextVisitSize;
    long long* dp = (long long*)calloc((size_t)n, sizeof(long long));
    for (int i = 1; i < n; i++) {
        dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2) % MOD;
        if (dp[i] < 0) dp[i] += MOD;
    }
    int ans = (int)dp[n - 1];
    free(dp);
    return ans;
}
