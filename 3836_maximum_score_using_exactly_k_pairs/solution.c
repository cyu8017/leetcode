// LeetCode 3836 - Maximum Score Using Exactly K Pairs
// https://leetcode.com/problems/maximum-score-using-exactly-k-pairs/

#include <stdlib.h>
#include <limits.h>

long long maxScore(int* nums1, int nums1Size, int* nums2, int nums2Size, int K) {
    int n = nums1Size, m = nums2Size;
    long long NEG = LLONG_MIN / 4;
    long long*** f = (long long***)malloc((size_t)(n + 1) * sizeof(long long**));
    for (int i = 0; i <= n; i++) {
        f[i] = (long long**)malloc((size_t)(m + 1) * sizeof(long long*));
        for (int j = 0; j <= m; j++) {
            f[i][j] = (long long*)malloc((size_t)(K + 1) * sizeof(long long));
            for (int k = 0; k <= K; k++) f[i][j][k] = NEG;
        }
    }
    f[0][0][0] = 0;
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= m; j++) {
            for (int k = 0; k <= K; k++) {
                if (i > 0 && f[i - 1][j][k] > f[i][j][k]) f[i][j][k] = f[i - 1][j][k];
                if (j > 0 && f[i][j - 1][k] > f[i][j][k]) f[i][j][k] = f[i][j - 1][k];
                if (i > 0 && j > 0 && k > 0) {
                    long long cand = f[i - 1][j - 1][k - 1] + (long long)nums1[i - 1] * nums2[j - 1];
                    if (cand > f[i][j][k]) f[i][j][k] = cand;
                }
            }
        }
    }
    long long ans = f[n][m][K];
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= m; j++) free(f[i][j]);
        free(f[i]);
    }
    free(f);
    return ans;
}
