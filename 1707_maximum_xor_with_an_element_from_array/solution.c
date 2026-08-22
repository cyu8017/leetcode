// LeetCode 1707 - Maximum XOR With an Element From Array
// https://leetcode.com/problems/maximum-xor-with-an-element-from-array/

#include <stdlib.h>

typedef struct {
    int x;
    int limit;
    int index;
} Query;

static int compareInts(const void* a, const void* b) {
    int va = *(const int*)a;
    int vb = *(const int*)b;
    return (va > vb) - (va < vb);
}

static int compareQueries(const void* a, const void* b) {
    const Query* qa = (const Query*)a;
    const Query* qb = (const Query*)b;
    return (qa->limit > qb->limit) - (qa->limit < qb->limit);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maximizeXor(int* nums, int numsSize, int** queries, int queriesSize,
                 int* queriesColSize, int* returnSize) {
    int* sorted = (int*)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        sorted[i] = nums[i];
    }
    qsort(sorted, numsSize, sizeof(int), compareInts);

    Query* order = (Query*)malloc(queriesSize * sizeof(Query));
    for (int i = 0; i < queriesSize; i++) {
        order[i].x = queries[i][0];
        order[i].limit = queries[i][1];
        order[i].index = i;
    }
    qsort(order, queriesSize, sizeof(Query), compareQueries);

    int capacity = numsSize * 32 + 1;
    int (*children)[2] = malloc(capacity * sizeof(*children));
    children[0][0] = -1;
    children[0][1] = -1;
    int nodeCount = 1;

    int* ans = (int*)malloc(queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        ans[i] = -1;
    }

    int added = 0;
    for (int q = 0; q < queriesSize; q++) {
        int x = order[q].x;
        int limit = order[q].limit;
        while (added < numsSize && sorted[added] <= limit) {
            int node = 0;
            for (int bit = 31; bit >= 0; bit--) {
                int b = (sorted[added] >> bit) & 1;
                if (children[node][b] == -1) {
                    children[nodeCount][0] = -1;
                    children[nodeCount][1] = -1;
                    children[node][b] = nodeCount++;
                }
                node = children[node][b];
            }
            added++;
        }
        if (added == 0) {
            continue;
        }
        int node = 0;
        int value = 0;
        for (int bit = 31; bit >= 0; bit--) {
            int b = (x >> bit) & 1;
            int want = b ^ 1;
            if (children[node][want] != -1) {
                value |= 1 << bit;
                node = children[node][want];
            } else {
                node = children[node][b];
            }
        }
        ans[order[q].index] = value;
    }

    free(sorted);
    free(order);
    free(children);
    *returnSize = queriesSize;
    return ans;
}
