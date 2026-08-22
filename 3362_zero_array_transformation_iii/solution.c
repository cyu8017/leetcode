// LeetCode 3362 - Zero Array Transformation III
// https://leetcode.com/problems/zero-array-transformation-iii/

#include <stdlib.h>

static int cmp_q0(const void* a, const void* b) {
    int* const* pa = (int* const*)a; int* const* pb = (int* const*)b;
    return (*pa)[0] - (*pb)[0];
}
static void heap_up(int* h, int i) {
    while (i > 0) { int p = (i - 1) / 2; if (h[p] >= h[i]) break; int t = h[p]; h[p] = h[i]; h[i] = t; i = p; }
}
static void heap_down(int* h, int n, int i) {
    for (;;) {
        int l = 2 * i + 1, r = 2 * i + 2, s = i;
        if (l < n && h[l] > h[s]) s = l;
        if (r < n && h[r] > h[s]) s = r;
        if (s == i) break;
        int t = h[s]; h[s] = h[i]; h[i] = t; i = s;
    }
}

int maxRemoval(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize) {
    (void)queriesColSize;
    qsort(queries, queriesSize, sizeof(int*), cmp_q0);
    int n = numsSize, hn = 0, cap = queriesSize + 1;
    int* heap = (int*)malloc(cap * sizeof(int));
    int* diff = (int*)calloc(n + 1, sizeof(int));
    int j = 0, used = 0, cur = 0;
    for (int i = 0; i < n; i++) {
        cur += diff[i];
        while (j < queriesSize && queries[j][0] == i) {
            heap[hn] = queries[j][1]; heap_up(heap, hn); hn++; j++;
        }
        while (cur < nums[i]) {
            if (hn == 0 || heap[0] < i) { free(heap); free(diff); return -1; }
            int r = heap[0]; heap[0] = heap[--hn]; if (hn) heap_down(heap, hn, 0);
            cur++; diff[r + 1]--; used++;
        }
    }
    free(heap); free(diff);
    return queriesSize - used;
}
