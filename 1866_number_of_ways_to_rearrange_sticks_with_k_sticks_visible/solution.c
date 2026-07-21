// LeetCode 1866 - Number of Ways to Rearrange Sticks With K Sticks Visible
// https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/

#include <stdlib.h>
#include <string.h>

int rearrangeSticks(int n, int k) {
    const int MOD = 1000000007;
    if (k == 0 || k > n) return 0;
    long long* dp = (long long*)calloc((size_t)(n + 1) * (n + 1), sizeof(long long));
    dp[1 * (n + 1) + 1] = 1;
    for (int sticks = 2; sticks <= n; sticks++) {
        dp[sticks * (n + 1) + 1] = (sticks - 1) * dp[(sticks - 1) * (n + 1) + 1] % MOD;
        for (int visible = 2; visible <= sticks; visible++) {
            dp[sticks * (n + 1) + visible] =
                (dp[(sticks - 1) * (n + 1) + visible - 1] +
                 (sticks - 1) * dp[(sticks - 1) * (n + 1) + visible]) %
                MOD;
        }
    }
    int answer = (int)dp[n * (n + 1) + k];
    free(dp);
    return answer;
}
