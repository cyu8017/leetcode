// LeetCode 0956 - Tallest Billboard
// https://leetcode.com/problems/tallest-billboard/

#include <stdlib.h>
#include <string.h>

int tallestBillboard(int* rods, int rodsSize) {
    int sum = 0;
    for (int i = 0; i < rodsSize; i++) sum += rods[i];
    int* dp = (int*)malloc((size_t)(sum + 1) * sizeof(int));
    for (int i = 0; i <= sum; i++) dp[i] = -1;
    dp[0] = 0;
    int* ndp = (int*)malloc((size_t)(sum + 1) * sizeof(int));
    for (int ri = 0; ri < rodsSize; ri++) {
        int rod = rods[ri];
        memcpy(ndp, dp, (size_t)(sum + 1) * sizeof(int));
        for (int diff = 0; diff <= sum; diff++) {
            if (dp[diff] < 0) continue;
            int taller = dp[diff];
            if (diff + rod <= sum && taller + rod > ndp[diff + rod]) ndp[diff + rod] = taller + rod;
            int nd = diff >= rod ? diff - rod : rod - diff;
            int nt = diff >= rod ? taller : taller - diff + rod;
            if (nd <= sum && nt > ndp[nd]) ndp[nd] = nt;
        }
        int* tmp = dp; dp = ndp; ndp = tmp;
    }
    int ans = dp[0] < 0 ? 0 : dp[0];
    free(dp); free(ndp);
    return ans;
}
