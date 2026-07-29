// LeetCode 0823 - Binary Trees With Factors
// https://leetcode.com/problems/binary-trees-with-factors/

#include <stdlib.h>

#define MOD 1000000007

static int cmp_int(const void* a, const void* b) {
    return (*(const int*)a) - (*(const int*)b);
}

int numFactoredBinaryTrees(int* arr, int arrSize) {
    qsort(arr, (size_t)arrSize, sizeof(int), cmp_int);
    long long* dp = (long long*)malloc((size_t)arrSize * sizeof(long long));
    int ans = 0;
    for (int i = 0; i < arrSize; i++) {
        dp[i] = 1;
        for (int j = 0; j < i; j++) {
            if (arr[i] % arr[j] == 0) {
                int right = arr[i] / arr[j];
                // binary search right
                int lo = 0, hi = i - 1, found = -1;
                while (lo <= hi) {
                    int mid = (lo + hi) / 2;
                    if (arr[mid] == right) { found = mid; break; }
                    if (arr[mid] < right) lo = mid + 1;
                    else hi = mid - 1;
                }
                if (found >= 0) dp[i] = (dp[i] + dp[j] * dp[found]) % MOD;
            }
        }
        ans = (int)((ans + dp[i]) % MOD);
    }
    free(dp);
    return ans;
}
