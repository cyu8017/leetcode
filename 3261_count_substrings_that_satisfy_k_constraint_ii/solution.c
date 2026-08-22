// LeetCode 3261 - Count Substrings That Satisfy K-Constraint II
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/

#include <stdlib.h>
#include <string.h>

long long* countKConstraintSubstrings(char* s, int k, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int n = (int)strlen(s);
    int* leftMost = (int*)malloc((size_t)n * sizeof(int));
    int z = 0, o = 0, L = 0;
    for (int R = 0; R < n; R++) {
        if (s[R] == '0') z++; else o++;
        while (z > k && o > k) {
            if (s[L] == '0') z--; else o--;
            L++;
        }
        leftMost[R] = L;
    }
    long long* pref = (long long*)calloc((size_t)(n + 1), sizeof(long long));
    for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + (i - leftMost[i] + 1);
    long long* ans = (long long*)malloc((size_t)queriesSize * sizeof(long long));
    for (int qi = 0; qi < queriesSize; qi++) {
        int l = queries[qi][0], r = queries[qi][1];
        int lo = l, hi = r + 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (leftMost[mid] < l) lo = mid + 1;
            else hi = mid;
        }
        long long res = 0;
        if (lo > l) {
            long long m = lo - l;
            res += m * (m + 1) / 2;
        }
        if (lo <= r) res += pref[r + 1] - pref[lo];
        ans[qi] = res;
    }
    free(leftMost); free(pref);
    *returnSize = queriesSize;
    return ans;
}
