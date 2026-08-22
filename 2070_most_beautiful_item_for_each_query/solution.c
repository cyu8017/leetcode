// LeetCode 2070 - Most Beautiful Item for Each Query
// https://leetcode.com/problems/most-beautiful-item-for-each-query/

#include <stdlib.h>

static int cmpItem(const void* a, const void* b) {
    int* const* ia = (int* const*)a;
    int* const* ib = (int* const*)b;
    return (*ia)[0] - (*ib)[0];
}

int* maximumBeauty(int** items, int itemsSize, int* itemsColSize, int* queries, int queriesSize, int* returnSize) {
    (void)itemsColSize;
    qsort(items, (size_t)itemsSize, sizeof(int*), cmpItem);
    int maxB = 0;
    for (int i = 0; i < itemsSize; i++) {
        if (items[i][1] > maxB) maxB = items[i][1];
        items[i][1] = maxB;
    }
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        int q = queries[i];
        int lo = 0, hi = itemsSize;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (items[mid][0] <= q) lo = mid + 1;
            else hi = mid;
        }
        ans[i] = lo == 0 ? 0 : items[lo - 1][1];
    }
    *returnSize = queriesSize;
    return ans;
}
