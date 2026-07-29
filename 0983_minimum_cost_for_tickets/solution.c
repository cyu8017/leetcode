// LeetCode 0983 - Minimum Cost For Tickets
// https://leetcode.com/problems/minimum-cost-for-tickets/

#include <stdlib.h>
#include <string.h>

int mincostTickets(int* days, int daysSize, int* costs, int costsSize) {
    (void)costsSize;
    int last = days[daysSize - 1];
    char* need = (char*)calloc((size_t)(last + 1), 1);
    for (int i = 0; i < daysSize; i++) need[days[i]] = 1;
    int* dp = (int*)calloc((size_t)(last + 1), sizeof(int));
    for (int d = 1; d <= last; d++) {
        if (!need[d]) dp[d] = dp[d - 1];
        else {
            int a = dp[d - 1] + costs[0];
            int b = dp[d - 7 > 0 ? d - 7 : 0] + costs[1];
            int c = dp[d - 30 > 0 ? d - 30 : 0] + costs[2];
            dp[d] = a < b ? a : b;
            if (c < dp[d]) dp[d] = c;
        }
    }
    int ans = dp[last];
    free(need); free(dp);
    return ans;
}
