// LeetCode 3668 - Restore Finishing Order
// https://leetcode.com/problems/restore-finishing-order/

#include <stdlib.h>

static int* g_order_pos;

static int cmpFriends(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return g_order_pos[x] - g_order_pos[y];
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* recoverOrder(int* order, int orderSize, int* friends, int friendsSize, int* returnSize) {
    int n = orderSize;
    int* d = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i < n; i++) d[order[i]] = i;
    int* ans = (int*)malloc((size_t)friendsSize * sizeof(int));
    for (int i = 0; i < friendsSize; i++) ans[i] = friends[i];
    g_order_pos = d;
    qsort(ans, (size_t)friendsSize, sizeof(int), cmpFriends);
    free(d);
    *returnSize = friendsSize;
    return ans;
}
