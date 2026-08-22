// LeetCode 1086 - High Five
// https://leetcode.com/problems/high-five/

#include <stdlib.h>
#include <string.h>

static int cmpDesc(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** highFive(int** items, int itemsSize, int* itemsColSize, int* returnSize, int** returnColumnSizes) {
    (void)itemsColSize;
    int scores[1001][50];
    int counts[1001];
    memset(counts, 0, sizeof(counts));
    int maxId = 0;
    for (int i = 0; i < itemsSize; i++) {
        int id = items[i][0];
        int score = items[i][1];
        if (id > maxId) {
            maxId = id;
        }
        scores[id][counts[id]++] = score;
    }
    int cap = 64;
    int** ans = (int**)malloc((size_t)cap * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)cap * sizeof(int));
    int count = 0;
    for (int id = 1; id <= maxId; id++) {
        if (counts[id] == 0) {
            continue;
        }
        qsort(scores[id], (size_t)counts[id], sizeof(int), cmpDesc);
        int sum = 0;
        for (int k = 0; k < 5; k++) {
            sum += scores[id][k];
        }
        if (count == cap) {
            cap *= 2;
            ans = (int**)realloc(ans, (size_t)cap * sizeof(int*));
            *returnColumnSizes = (int*)realloc(*returnColumnSizes, (size_t)cap * sizeof(int));
        }
        ans[count] = (int*)malloc(2 * sizeof(int));
        ans[count][0] = id;
        ans[count][1] = sum / 5;
        (*returnColumnSizes)[count] = 2;
        count++;
    }
    *returnSize = count;
    return ans;
}
