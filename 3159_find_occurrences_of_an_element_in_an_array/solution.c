// LeetCode 3159 - Find Occurrences of an Element in an Array
// https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

#include <stdlib.h>

int* occurrencesOfElement(int* nums, int numsSize, int* queries, int queriesSize, int x, int* returnSize) {
    int* ids = malloc(numsSize * sizeof(int));
    int idn = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] == x) ids[idn++] = i;
    int* ans = malloc(queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++)
        ans[i] = (queries[i] - 1 < idn) ? ids[queries[i] - 1] : -1;
    free(ids);
    *returnSize = queriesSize;
    return ans;
}
