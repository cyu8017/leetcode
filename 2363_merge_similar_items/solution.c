// LeetCode 2363 - Merge Similar Items
// https://leetcode.com/problems/merge-similar-items/

#include <stdlib.h>
#include <string.h>

static int cmpInt(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int** mergeSimilarItems(int** items1, int items1Size, int* items1ColSize, int** items2, int items2Size, int* items2ColSize, int* returnSize, int** returnColumnSizes) {
    (void)items1ColSize; (void)items2ColSize;
    int mp[1001] = {0};
    for (int i = 0; i < items1Size; i++) mp[items1[i][0]] += items1[i][1];
    for (int i = 0; i < items2Size; i++) mp[items2[i][0]] += items2[i][1];
    int keys[1001], kc = 0;
    for (int v = 1; v <= 1000; v++) if (mp[v]) keys[kc++] = v;
    int** ans = (int**)malloc((size_t)kc * sizeof(int*));
    int* cols = (int*)malloc((size_t)kc * sizeof(int));
    for (int i = 0; i < kc; i++) {
        ans[i] = (int*)malloc(2 * sizeof(int));
        ans[i][0] = keys[i];
        ans[i][1] = mp[keys[i]];
        cols[i] = 2;
    }
    *returnSize = kc;
    *returnColumnSizes = cols;
    return ans;
}
