// LeetCode 2747 - Count Zero Request Servers
// https://leetcode.com/problems/count-zero-request-servers/

#include <stdlib.h>
#include <string.h>

typedef struct { int t, i; } Qi2747;

static int cmpLogs2747(const void* a, const void* b) {
    int* const* aa = (int* const*)a;
    int* const* bb = (int* const*)b;
    return (*aa)[1] - (*bb)[1];
}
static int cmpQi2747(const void* a, const void* b) {
    return ((const Qi2747*)a)->t - ((const Qi2747*)b)->t;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countServers(int n, int** logs, int logsSize, int* logsColSize, int x, int* queries, int queriesSize, int* returnSize) {
    (void)logsColSize;
    if (logsSize > 0) qsort(logs, (size_t)logsSize, sizeof(int*), cmpLogs2747);
    Qi2747* qs = (Qi2747*)malloc((size_t)queriesSize * sizeof(Qi2747));
    for (int i = 0; i < queriesSize; i++) qs[i] = (Qi2747){queries[i], i};
    qsort(qs, (size_t)queriesSize, sizeof(Qi2747), cmpQi2747);
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    int* cnt = (int*)calloc((size_t)(n + 1), sizeof(int));
    int active = 0, l = 0, r = 0;
    for (int qi = 0; qi < queriesSize; qi++) {
        while (r < logsSize && logs[r][1] <= qs[qi].t) {
            int id = logs[r][0];
            if (cnt[id] == 0) active++;
            cnt[id]++;
            r++;
        }
        while (l < r && logs[l][1] < qs[qi].t - x) {
            int id = logs[l][0];
            cnt[id]--;
            if (cnt[id] == 0) active--;
            l++;
        }
        ans[qs[qi].i] = n - active;
    }
    free(qs); free(cnt);
    *returnSize = queriesSize;
    return ans;
}
