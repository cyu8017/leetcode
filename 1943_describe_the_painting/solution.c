// LeetCode 1943 - Describe the Painting
// https://leetcode.com/problems/describe-the-painting/

#include <stdlib.h>

typedef struct { int pos; long long delta; } Ev;

static int cmpEv(const void* a, const void* b) {
    return ((const Ev*)a)->pos - ((const Ev*)b)->pos;
}

long long** splitPainting(int** segments, int segmentsSize, int* segmentsColSize, int* returnSize, int** returnColumnSizes) {
    (void)segmentsColSize;
    Ev* ev = (Ev*)malloc((size_t)segmentsSize * 2 * sizeof(Ev));
    for (int i = 0; i < segmentsSize; i++) {
        ev[2 * i].pos = segments[i][0];
        ev[2 * i].delta = segments[i][2];
        ev[2 * i + 1].pos = segments[i][1];
        ev[2 * i + 1].delta = -segments[i][2];
    }
    int m = segmentsSize * 2;
    qsort(ev, (size_t)m, sizeof(Ev), cmpEv);
    long long** ans = (long long**)malloc((size_t)m * sizeof(long long*));
    *returnColumnSizes = (int*)malloc((size_t)m * sizeof(int));
    int sz = 0;
    long long cur = 0;
    int i = 0;
    while (i < m) {
        int pos = ev[i].pos;
        while (i < m && ev[i].pos == pos) {
            cur += ev[i].delta;
            i++;
        }
        if (i < m && cur) {
            ans[sz] = (long long*)malloc(3 * sizeof(long long));
            ans[sz][0] = pos;
            ans[sz][1] = ev[i].pos;
            ans[sz][2] = cur;
            (*returnColumnSizes)[sz] = 3;
            sz++;
        }
    }
    free(ev);
    *returnSize = sz;
    return ans;
}
