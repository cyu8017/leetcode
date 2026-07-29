// LeetCode 1187 - Make Array Strictly Increasing
// https://leetcode.com/problems/make-array-strictly-increasing/

#include <limits.h>
#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

typedef struct {
    int val;
    int ops;
} DpEntry;

int makeArrayIncreasing(int* arr1, int arr1Size, int* arr2, int arr2Size) {
    qsort(arr2, (size_t)arr2Size, sizeof(int), cmpInt);
    int uniq[arr2Size];
    int uniqSize = 0;
    for (int i = 0; i < arr2Size; i++) {
        if (i == 0 || arr2[i] != arr2[i - 1]) uniq[uniqSize++] = arr2[i];
    }
    DpEntry* dp = (DpEntry*)malloc((size_t)(uniqSize + 1) * sizeof(DpEntry));
    int dpSize = 1;
    dp[0].val = -1;
    dp[0].ops = 0;
    for (int idx = 0; idx < arr1Size; idx++) {
        int num = arr1[idx];
        DpEntry* ndp = (DpEntry*)malloc((size_t)(uniqSize + 1) * sizeof(DpEntry));
        int ndpSize = 0;
        for (int i = 0; i < dpSize; i++) {
            int prev = dp[i].val;
            int ops = dp[i].ops;
            if (num > prev) {
                ndp[ndpSize].val = num;
                ndp[ndpSize].ops = ops;
                ndpSize++;
            }
            int lo = 0, hi = uniqSize;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (uniq[mid] <= prev) lo = mid + 1;
                else hi = mid;
            }
            if (lo < uniqSize) {
                int chosen = uniq[lo];
                int found = -1;
                for (int j = 0; j < ndpSize; j++) {
                    if (ndp[j].val == chosen) {
                        found = j;
                        break;
                    }
                }
                if (found >= 0) {
                    if (ops + 1 < ndp[found].ops) ndp[found].ops = ops + 1;
                } else {
                    ndp[ndpSize].val = chosen;
                    ndp[ndpSize].ops = ops + 1;
                    ndpSize++;
                }
            }
        }
        free(dp);
        if (ndpSize == 0) {
            free(ndp);
            return -1;
        }
        dp = ndp;
        dpSize = ndpSize;
    }
    int ans = INT_MAX;
    for (int i = 0; i < dpSize; i++) {
        if (dp[i].ops < ans) ans = dp[i].ops;
    }
    free(dp);
    return ans;
}
