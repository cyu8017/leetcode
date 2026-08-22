// LeetCode 2736 - Maximum Sum Queries
// https://leetcode.com/problems/maximum-sum-queries/

#include <stdlib.h>
#include <string.h>

typedef struct { int x, y, s; } Pair2736;
typedef struct { int x, y, i; } Qi2736;

static int cmpPts2736(const void* a, const void* b) {
    return ((const Pair2736*)b)->x - ((const Pair2736*)a)->x;
}
static int cmpQs2736(const void* a, const void* b) {
    return ((const Qi2736*)b)->x - ((const Qi2736*)a)->x;
}
static int cmpInt2736(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static int rank2736(int* uniq, int m, int y) {
    int lo = 0, hi = m - 1;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if (uniq[mid] == y) return mid + 1;
        if (uniq[mid] < y) lo = mid + 1;
        else hi = mid - 1;
    }
    return 1;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maximumSumQueries(int* nums1, int nums1Size, int* nums2, int nums2Size, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)nums2Size; (void)queriesColSize;
    int n = nums1Size;
    Pair2736* pts = (Pair2736*)malloc((size_t)n * sizeof(Pair2736));
    for (int i = 0; i < n; i++)
        pts[i] = (Pair2736){nums1[i], nums2[i], nums1[i] + nums2[i]};
    qsort(pts, (size_t)n, sizeof(Pair2736), cmpPts2736);
    Qi2736* qs = (Qi2736*)malloc((size_t)queriesSize * sizeof(Qi2736));
    for (int i = 0; i < queriesSize; i++)
        qs[i] = (Qi2736){queries[i][0], queries[i][1], i};
    qsort(qs, (size_t)queriesSize, sizeof(Qi2736), cmpQs2736);

    int* ys = (int*)malloc((size_t)(n + queriesSize) * sizeof(int));
    int ysz = 0;
    for (int i = 0; i < n; i++) ys[ysz++] = nums2[i];
    for (int i = 0; i < queriesSize; i++) ys[ysz++] = queries[i][1];
    qsort(ys, (size_t)ysz, sizeof(int), cmpInt2736);
    int* uniq = (int*)malloc((size_t)ysz * sizeof(int));
    int m = 0;
    for (int i = 0; i < ysz; i++)
        if (m == 0 || uniq[m - 1] != ys[i]) uniq[m++] = ys[i];
    free(ys);

    int* bit = (int*)calloc((size_t)(m + 2), sizeof(int));
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    int j = 0;
    for (int qi = 0; qi < queriesSize; qi++) {
        while (j < n && pts[j].x >= qs[qi].x) {
            int idx = m - rank2736(uniq, m, pts[j].y) + 1;
            for (int ii = idx; ii <= m; ii += ii & -ii)
                if (pts[j].s > bit[ii]) bit[ii] = pts[j].s;
            j++;
        }
        int idx = m - rank2736(uniq, m, qs[qi].y) + 1;
        int best = -1;
        for (int ii = idx; ii > 0; ii -= ii & -ii)
            if (bit[ii] > best) best = bit[ii];
        ans[qs[qi].i] = best;
    }
    free(pts); free(qs); free(uniq); free(bit);
    *returnSize = queriesSize;
    return ans;
}
