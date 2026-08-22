// LeetCode 2940 - Find Building Where Alice and Bob Can Meet
// https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

#include <stdlib.h>

typedef struct { int h, qi; } Item;
typedef struct { int h, idx; } Stack;

int* leftmostBuildingQueries(int* heights, int heightsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int n = heightsSize;
    int* ans = (int*)malloc(queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) ans[i] = -1;
    Item** buckets = (Item**)calloc(n, sizeof(Item*));
    int* bsz = (int*)calloc(n, sizeof(int));
    int* bcap = (int*)calloc(n, sizeof(int));
    for (int qi = 0; qi < queriesSize; qi++) {
        int a = queries[qi][0], b = queries[qi][1];
        if (a > b) { int t = a; a = b; b = t; }
        if (a == b || heights[a] < heights[b]) { ans[qi] = b; continue; }
        if (bsz[b] == bcap[b]) { bcap[b] = bcap[b] ? bcap[b]*2 : 4; buckets[b] = (Item*)realloc(buckets[b], bcap[b]*sizeof(Item)); }
        buckets[b][bsz[b]++] = (Item){heights[a], qi};
    }
    Stack* st = (Stack*)malloc(n * sizeof(Stack));
    int top = 0;
    for (int i = n - 1; i >= 0; i--) {
        for (int j = 0; j < bsz[i]; j++) {
            Item it = buckets[i][j];
            int lo = 0, hi = top - 1, pos = -1;
            while (lo <= hi) {
                int mid = (lo + hi) / 2;
                if (st[mid].h > it.h) { pos = st[mid].idx; lo = mid + 1; }
                else hi = mid - 1;
            }
            ans[it.qi] = pos;
        }
        while (top > 0 && st[top - 1].h <= heights[i]) top--;
        st[top++] = (Stack){heights[i], i};
    }
    for (int i = 0; i < n; i++) free(buckets[i]);
    free(buckets); free(bsz); free(bcap); free(st);
    *returnSize = queriesSize;
    return ans;
}
