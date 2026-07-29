// LeetCode 0879 - Profitable Schemes
// https://leetcode.com/problems/profitable-schemes/

#include <stdlib.h>

#define MOD 1000000007
#define MIN(a,b) ((a)<(b)?(a):(b))

int profitableSchemes(int n, int minProfit, int* group, int groupSize, int* profit, int profitSize) {
    (void)profitSize;
    int** dp = (int**)malloc((size_t)(n + 1) * sizeof(int*));
    for (int i = 0; i <= n; i++) dp[i] = (int*)calloc((size_t)minProfit + 1, sizeof(int));
    dp[0][0] = 1;
    for (int g = 0; g < groupSize; g++) {
        int members = group[g], p = profit[g];
        for (int people = n; people >= members; people--) {
            for (int prof = minProfit; prof >= 0; prof--) {
                int np = MIN(minProfit, prof + p);
                dp[people][np] = (dp[people][np] + dp[people - members][prof]) % MOD;
            }
        }
    }
    int ans = 0;
    for (int people = 0; people <= n; people++)
        ans = (ans + dp[people][minProfit]) % MOD;
    for (int i = 0; i <= n; i++) free(dp[i]);
    free(dp);
    return ans;
}
