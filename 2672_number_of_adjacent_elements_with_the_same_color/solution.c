// LeetCode 2672 - Number of Adjacent Elements With the Same Color
// https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* colorTheArray(int n, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int* colors = (int*)calloc((size_t)n, sizeof(int));
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    int same = 0;
    for (int i = 0; i < queriesSize; i++) {
        int idx = queries[i][0], color = queries[i][1];
        if (colors[idx] != 0) {
            if (idx > 0 && colors[idx] == colors[idx - 1]) same--;
            if (idx + 1 < n && colors[idx] == colors[idx + 1]) same--;
        }
        colors[idx] = color;
        if (idx > 0 && colors[idx] == colors[idx - 1]) same++;
        if (idx + 1 < n && colors[idx] == colors[idx + 1]) same++;
        ans[i] = same;
    }
    free(colors);
    *returnSize = queriesSize;
    return ans;
}
