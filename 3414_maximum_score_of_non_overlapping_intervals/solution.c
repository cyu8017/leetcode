// LeetCode 3414 - Maximum Score of Non-overlapping Intervals
// https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

#include <stdlib.h>
#include <string.h>

typedef struct { int l, r, w, i; } It;

static int cmp_it(const void* a, const void* b) { return ((const It*)a)->r - ((const It*)b)->r; }
static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

static int better_idx(long long sa, int* ia, int na, long long sb, int* ib, int nb) {
    if (sa != sb) return sa > sb ? 1 : 0;
    int m = na < nb ? na : nb;
    for (int i = 0; i < m; i++) if (ia[i] != ib[i]) return ia[i] < ib[i] ? 1 : 0;
    return na <= nb ? 1 : 0;
}

int* maximumWeight(int** intervals, int intervalsSize, int* intervalsColSize, int* returnSize) {
    (void)intervalsColSize;
    int n = intervalsSize;
    It* arr = (It*)malloc(n * sizeof(It));
    for (int i = 0; i < n; i++) arr[i] = (It){intervals[i][0], intervals[i][1], intervals[i][2], i};
    qsort(arr, n, sizeof(It), cmp_it);

    long long score[n + 1][5];
    int* idx[n + 1][5];
    int len[n + 1][5];
    memset(score, 0, sizeof(score));
    memset(idx, 0, sizeof(idx));
    memset(len, 0, sizeof(len));

    for (int i = 1; i <= n; i++) {
        It cur = arr[i - 1];
        for (int t = 0; t <= 4; t++) {
            score[i][t] = score[i - 1][t];
            len[i][t] = len[i - 1][t];
            if (len[i][t]) {
                idx[i][t] = (int*)malloc(len[i][t] * sizeof(int));
                memcpy(idx[i][t], idx[i - 1][t], len[i][t] * sizeof(int));
            } else idx[i][t] = NULL;
        }
        int lo = 0, hi = i - 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (arr[mid].r >= cur.l) hi = mid; else lo = mid + 1;
        }
        int prev = lo;
        for (int t = 1; t <= 4; t++) {
            long long ns = score[prev][t - 1] + cur.w;
            int nl = len[prev][t - 1] + 1;
            int* ni = (int*)malloc(nl * sizeof(int));
            if (len[prev][t - 1]) memcpy(ni, idx[prev][t - 1], len[prev][t - 1] * sizeof(int));
            ni[nl - 1] = cur.i;
            qsort(ni, nl, sizeof(int), cmp_int);
            if (better_idx(ns, ni, nl, score[i][t], idx[i][t], len[i][t])) {
                free(idx[i][t]);
                score[i][t] = ns; idx[i][t] = ni; len[i][t] = nl;
            } else free(ni);
        }
    }
    int bt = 0;
    for (int t = 1; t <= 4; t++)
        if (better_idx(score[n][t], idx[n][t], len[n][t], score[n][bt], idx[n][bt], len[n][bt])) bt = t;
    *returnSize = len[n][bt];
    int* ans = (int*)malloc((*returnSize ? *returnSize : 1) * sizeof(int));
    if (*returnSize) memcpy(ans, idx[n][bt], *returnSize * sizeof(int));
    for (int i = 0; i <= n; i++) for (int t = 0; t <= 5; t++) {}
    for (int i = 0; i <= n; i++) for (int t = 0; t <= 4; t++) free(idx[i][t]);
    free(arr);
    return ans;
}
