// LeetCode 2035 - Partition Array Into Two Arrays to Minimize Sum Difference
// https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

#include <stdlib.h>
#include <limits.h>

static int cmpInt(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

static void sumsByCount(int* arr, int m, int*** out, int** outCnt) {
    *out = (int**)calloc((size_t)m + 1, sizeof(int*));
    *outCnt = (int*)calloc((size_t)m + 1, sizeof(int));
    int caps[20] = {0};
    for (int mask = 0; mask < (1 << m); mask++) {
        int sum = 0, c = 0;
        for (int i = 0; i < m; i++) if (mask & (1 << i)) { sum += arr[i]; c++; }
        if ((*outCnt)[c] == caps[c]) {
            caps[c] = caps[c] ? caps[c] * 2 : 8;
            (*out)[c] = (int*)realloc((*out)[c], (size_t)caps[c] * sizeof(int));
        }
        (*out)[c][(*outCnt)[c]++] = sum;
    }
    for (int i = 0; i <= m; i++) qsort((*out)[i], (size_t)(*outCnt)[i], sizeof(int), cmpInt);
}

int minimumDifference(int* nums, int numsSize) {
    int n = numsSize / 2;
    int total = 0;
    for (int i = 0; i < numsSize; i++) total += nums[i];
    int *Lcnt, *Rcnt;
    int **L, **R;
    sumsByCount(nums, n, &L, &Lcnt);
    sumsByCount(nums + n, n, &R, &Rcnt);
    int ans = INT_MAX;
    for (int k = 0; k <= n; k++) {
        for (int i = 0; i < Lcnt[k]; i++) {
            int s1 = L[k][i];
            int need = total / 2 - s1;
            int* arr = R[n - k];
            int sz = Rcnt[n - k];
            int lo = 0, hi = sz;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (arr[mid] < need) lo = mid + 1;
                else hi = mid;
            }
            for (int t = 0; t < 2; t++) {
                int idx = lo - 1 + t;
                if (idx >= 0 && idx < sz) {
                    int s2 = arr[idx];
                    int diff = total - 2 * (s1 + s2);
                    if (diff < 0) diff = -diff;
                    if (diff < ans) ans = diff;
                }
            }
        }
    }
    for (int i = 0; i <= n; i++) { free(L[i]); free(R[i]); }
    free(L); free(R); free(Lcnt); free(Rcnt);
    return ans;
}
