// LeetCode 3501 - Maximize Active Section with Trade II
// https://leetcode.com/problems/maximize-active-section-with-trade-ii/

#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxActiveSectionsAfterTrade(char* s, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queries; (void)queriesColSize;
    int ones = 0;
    for (int i = 0; s[i]; i++) if (s[i] == '1') ones++;
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) ans[i] = ones;
    *returnSize = queriesSize;
    return ans;
}
