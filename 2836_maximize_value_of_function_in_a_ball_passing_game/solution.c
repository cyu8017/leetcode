// LeetCode 2836 - Maximize Value of Function in a Ball Passing Game
// https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

#include <stdlib.h>

long long getMaxFunctionValue(int* receiver, int receiverSize, long long k) {
    int n = receiverSize;
    const int LOG = 36;
    int** up = (int**)malloc(LOG * sizeof(int*));
    long long** sum = (long long**)malloc(LOG * sizeof(long long*));
    for (int j = 0; j < LOG; j++) {
        up[j] = (int*)malloc(n * sizeof(int));
        sum[j] = (long long*)malloc(n * sizeof(long long));
    }
    for (int i = 0; i < n; i++) {
        up[0][i] = receiver[i];
        sum[0][i] = receiver[i];
    }
    for (int j = 1; j < LOG; j++) {
        for (int i = 0; i < n; i++) {
            int mid = up[j - 1][i];
            up[j][i] = up[j - 1][mid];
            sum[j][i] = sum[j - 1][i] + sum[j - 1][mid];
        }
    }
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        int cur = i;
        long long total = i;
        long long kk = k;
        for (int j = 0; j < LOG; j++) {
            if (kk & (1LL << j)) {
                total += sum[j][cur];
                cur = up[j][cur];
            }
        }
        if (total > ans) ans = total;
    }
    for (int j = 0; j < LOG; j++) { free(up[j]); free(sum[j]); }
    free(up); free(sum);
    return ans;
}
