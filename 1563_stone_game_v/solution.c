// LeetCode 1563 - Stone Game V
// https://leetcode.com/problems/stone-game-v/

#include <stdlib.h>

int stoneGameV(int* stoneValue, int stoneValueSize) {
    int n = stoneValueSize;
    if (n == 0) return 0;
    int* pre = (int*)malloc((size_t)(n + 1) * sizeof(int));
    pre[0] = 0;
    for (int i = 0; i < n; i++) pre[i + 1] = pre[i] + stoneValue[i];

    int** dp = (int**)malloc((size_t)n * sizeof(int*));
    int** left = (int**)malloc((size_t)n * sizeof(int*));
    int** right = (int**)malloc((size_t)n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        dp[i] = (int*)calloc((size_t)n, sizeof(int));
        left[i] = (int*)calloc((size_t)n, sizeof(int));
        right[i] = (int*)calloc((size_t)n, sizeof(int));
        left[i][i] = right[i][i] = stoneValue[i];
    }

    for (int length = 2; length <= n; length++) {
        for (int i = 0; i + length - 1 < n; i++) {
            int j = i + length - 1;
            int lo = i, hi = j - 1;
            while (lo <= hi) {
                int mid = (lo + hi) / 2;
                if (2 * (pre[mid + 1] - pre[i]) >= pre[j + 1] - pre[i]) hi = mid - 1;
                else lo = mid + 1;
            }
            int split = lo;
            int left_sum = pre[split + 1] - pre[i];
            int right_sum = pre[j + 1] - pre[split + 1];
            int best = right[split + 1][j];
            if (left_sum == right_sum) {
                if (left[i][split] > best) best = left[i][split];
            } else if (split > i) {
                if (left[i][split - 1] > best) best = left[i][split - 1];
            }
            dp[i][j] = best;
            int total = pre[j + 1] - pre[i];
            left[i][j] = left[i][j - 1] > total + best ? left[i][j - 1] : total + best;
            right[i][j] = right[i + 1][j] > total + best ? right[i + 1][j] : total + best;
        }
    }
    int ans = dp[0][n - 1];
    for (int i = 0; i < n; i++) { free(dp[i]); free(left[i]); free(right[i]); }
    free(dp); free(left); free(right); free(pre);
    return ans;
}
